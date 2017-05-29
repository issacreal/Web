import requests
import json
import pickle

#targetUrl = "http://www.tse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=19990515"
baseUrl = "http://www.tse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date="



startYear   = 2010
startMonth  = 9
endYear     = 2017
endMonth  = 5


def GetData(year,month):
    yy = str(year)
    mm = str(month)
    
    if(month < 10):
        mm =  "0" + mm

    targetUrl = baseUrl + yy + mm + "01"
    print(targetUrl)

    res = requests.get(targetUrl)
    #print(res.text)
    data =  json.loads(res.text)["data"]
   
    '''
    for e in data:
        print(e)
    '''
    return data

q = GetData(startYear,1)
for year in range(startYear,endYear + 1):    
    for month in range(1,12 + 1):
        if(month < endMonth and year < endYear):
            q = q + GetData(year,month)

with open('outfile.txt', 'wb+') as fp:
   pickle.dump(q, fp)

with open('outfile.txt', 'rb') as fp:
    itemlist = pickle.load(fp)
    
#print(itemlist)    

for e in itemlist:
    print(e)   
    
