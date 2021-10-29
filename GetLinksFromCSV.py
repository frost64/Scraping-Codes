import pandas as pd

def extractLinks():
    a=pd.read_csv('DatasetLinks.csv',usecols=['Links']) # Use 'Name' column as index
    lsLink=a.values.tolist()
    allLinks=[]
    for i in range(10):
        eachLst=lsLink[i][0].split()
        for element in eachLst:
            allLinks.append(element[1:-1].strip('\''))
    return allLinks
PLink=extractLinks()

for i in PLink:
    print(i)
