import pandas as pd
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imdb.com/chart/top?sort=rk,asc&mode=simple&page=1')
soup = BeautifulSoup(r.text, 'html.parser')

result1 = soup.find_all('td', attrs={'class': 'titleColumn'})
result2 = soup.find_all('td', attrs={'class': 'ratingColumn imdbRating'})

store = {'Title': [], 'Celebrities': [], 'Movie Reference': [], 'Release Date': [], 'Imdb Rating': []}

for i in range(250):
    store['Title'].append(result1[i].find('a').text[:])
    names = result1[i].find('a')['title']
    store['Celebrities'].append(names)
    link = 'https://www.imdb.com' + result1[i].find('a')['href']
    store['Movie Reference'].append(link)
    store['Release Date'].append(result1[i].find('span').text[1:-1])
    store['Imdb Rating'].append(result2[i].find('strong').text[:])

df = pd.DataFrame(store)
df.to_csv('Imdb_top250.csv', index=False, encoding='utf-8')
