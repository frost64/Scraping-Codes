import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.gsmarena.com/samsung_galaxy_f42_5g-11124.php'
r = requests.get(url)
print (r.content)
soup = BeautifulSoup(r.content,'html5lib')
table = soup.find('div', attrs = {'specs-list'})
for row in table.findAll('div', attrs = {'specs-list'}):
    for li in link.find_all('li'):
            for anc in li.find_all('a'):
                print(anc)
