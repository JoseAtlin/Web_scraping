import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

r = requests.get('https://gadgets.ndtv.com/laptops/laptops-under-50000')
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'pd-lst-wrp kpc_lhs_widget'})

store = {'Name': [], 'Money': [], 'Display size': [], 'Display resolution': [], 'Touchscreen': [], 'Processor': [], 
        'RAM': [], 'OS': [], 'Hard disk': [], 'SSD': [], 'Graphics': [], 'Weight': []}
c = 0
for result in results:
    temp = 0
    for check in result.find_all('a'):
        if temp == 0:
            store['Name'].append(check.text[:])
        elif (temp == 2 or temp == 3) and (check.text[:][:3] == ' Rs'):
            store['Money'].append(check.text[:].replace(' ', '').replace('Rs.', ''))
        temp += 1
    
    temp = 0
    for check in result.find_all('td'):
        if temp >= 1:
            if temp % 2 != 0:
                ins = check.text[:]
            else:
                store[ins].append(check.text[:])

        temp += 1
    
    c += 1
        
    for i, v in store.items():
        if len(store[i]) < c:
            store[i].append(np.nan)

df = pd.DataFrame(store)
df.to_csv('Gadget_NDTV.csv', index=False, encoding='utf-8')
