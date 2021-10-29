import requests
import pandas as pd
from bs4 import BeautifulSoup

Dataset = {}

brandsRequired=["Samsung","Apple","Huawei","Sony","LG","Xiaomi","Oppo","Realme","OnePlus","vivo"]
def link_scan(link_url):
    c = 1
    source_code=requests.get(link_url)
    plain_text=source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.find_all('div',{'class':'brandmenu-v2 light l-box clearfix'}):
        for li in link.find_all('li'):
            for anc in li.find_all('a'):
                anc_src = r'http://www.gsmarena.com/' + anc.get('href')
                anc_name = anc.string
                if(anc_name in brandsRequired):
                    Dataset[anc_name]=[]
                    c += 1
                    inside_scan(anc_name, anc_src)


def inside_scan(name, hrefs):
    i = 1
    source_code=requests.get(hrefs)
    plain_text=source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.find_all('div',{'class':'makers'}):
        for li in link.find_all('li'):
            for anc in li.find_all('a'):
                anc_src = r'http://www.gsmarena.com/' + anc.get('href')
                for nam in (sp.find('span') for sp in anc.find_all('strong')):
                    modal_name = nam.string
                    Dataset[name].append(anc_src)
                    if(i>9):
                        return
                    else:
                        i += 1

link_scan(r'http://www.gsmarena.com')

# This will write the links in the dictionary 'Dataset' into csv file 'DatasetLinks.csv' using pandas 

dataFrame = pd.DataFrame(data=Dataset.items(), columns=['Brand', 'Links'])
print("DataFrame...\n",dataFrame)

# write dataFrame to DatasetLinks CSV file
dataFrame.to_csv("DatasetLinks.csv")


# display the contents of the output csv
print("The output csv file written successfully and generated...")
