import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "https://turquoise.health/providers/abbott-northwestern-hospital/information"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib')
c = 0
quote = {} 
for row in soup.findAll('div', attrs = {'class':'hospital-all-detail'}): 
    for j in row.findAll('ul'):
        for k in j.findAll('li'):
            c = c  + 1
            print("count==> ",c)
            print("span length ",k)
            if len(k.span) == 1:
                if c == 1:
                    quote['Name'] = k.span.text
                
                elif c == 2:
                    quote['ADDRESS'] = k.span.text
                elif c == 3:
                    quote['Phone'] = k.span.text
                
                elif c == 4:
                    quote['MEDICARE PROVIDER ID'] = k.span.text
                
                elif c == 5:
                    quote['NATIONAL PROVIDER ID (NPI)'] =k.span.text
                
                elif c == 7:
                    quote['PROVIDER TYPE'] = k.span.text
                
                elif c == 8:
                    quote['OWNERSHIP'] = k.span.text
                
                elif c == 9:
                    quote['BEDS'] = k.span.text
                
            


print(quote)