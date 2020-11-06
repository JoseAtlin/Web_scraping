import pandas as pd
import requests
from bs4 import BeautifulSoup

r = requests.get('https://gadgets.ndtv.com/laptops/laptops-under-50000')
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'pd-lst-wrp kpc_lhs_widget'})

records = []
for result in results:
    store1 = []
    temp1 = 0
    for check in result.find_all('a'):
        if temp1 == 0:
            store1.append(check.text[:])
        elif temp1 == 3:
            store1.append(check.text[:].replace(' ', '').replace('Rs.', ''))
        temp1 += 1

    store2 = []
    temp2 = 0
    for check in result.find_all('td'):
        if temp2 >= 2 and temp2 % 2 == 0:
            store2.append(check.text[:])
        temp2 += 1
    
    records.append(store1 + store2)

print(records)