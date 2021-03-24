import requests 
from bs4 import BeautifulSoup 
import csv
from csv import DictWriter  
   
URL = "https://turquoise.health/providers/sylvan-grove-hospital/information"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib')
c = 0
quotes=[]
quote = {} 
for row in soup.findAll('div', attrs = {'class':'hospital-all-detail'}): 
    for j in row.findAll('ul'):
        for k in j.findAll('li'):
            # c = c  + 1
            # print("count==> ",c)
            print("para ",k.p.text)
            if len(k.span) == 1:
                if k.p.text == 'Name':
                    quote['Name'] = k.span.text


                elif k.p.text == 'ADDRESS':
                    quote['ADDRESS'] = k.span.text
                
                
                elif k.p.text == 'Phone':
                    quote['Phone'] = k.span.text

               
                elif k.p.text == 'MEDICARE PROVIDER ID':
                    quote['MEDICARE PROVIDER ID'] = k.span.text
                
                elif k.p.text == 'NATIONAL PROVIDER ID (NPI)':
                    quote['NATIONAL PROVIDER ID (NPI)'] =k.span.text
                
                elif k.p.text == 'PROVIDER TYPE':
                    quote['PROVIDER TYPE'] = k.span.text
                
                elif k.p.text == 'OWNERSHIP':
                    quote['OWNERSHIP'] = k.span.text
                
                elif k.p.text == 'BEDS':
                    quote['BEDS'] = k.span.text
                
            else:
                # if c == 6:
                if k.p.text == 'WEBSITE':
                    if  k.span.a['href'] != "":
                        quote['WEBSITE'] = k.span.a['href']

                elif k.p.text == 'HEALTH SYSTEM AFFILIATION':
                    quote['HEALTH SYSTEM AFFILIATION'] = k.span.a['href']

                   
                        
              
        

quotes.append(quote)
print(quotes)
columnsName = ['Name','ADDRESS','Phone','MEDICARE PROVIDER ID','NATIONAL PROVIDER ID (NPI)','WEBSITE','PROVIDER TYPE','OWNERSHIP','BEDS','HEALTH SYSTEM AFFILIATION']
filename = 'hospital.csv'
# with open(filename, 'w', newline='') as f: 
#     w = csv.DictWriter(f,columnsName) 
#     w.writeheader() 
#     w.writerow(quotes[0])



# with open(filename, 'a', newline='') as f_object:
#     dictwriter_object = DictWriter(f_object, fieldnames = columnsName)
#     dictwriter_object.writerow(quotes[0])
        
  