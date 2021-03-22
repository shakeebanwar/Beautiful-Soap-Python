import requests 
from bs4 import BeautifulSoup 
import csv
from csv import DictWriter  
alllinks=[]  
for i in range(1,67): 
    URL = f"https://turquoise.health/providers?page={i}"
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib')

    for row in soup.findAll('div', attrs = {'class':'alphabet-wise-names'}): 
        for j in row.findAll('ul'):
            for k in j.findAll('li'):
                alllinks.append(k.a['href'])


print(alllinks)
           