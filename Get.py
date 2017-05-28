import requests
import json

#targetUrl = "http://www.tse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=19990515"
baseUrl = "http://www.tse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date="



year   = 2010
month  = 10

yy = str(year)
mm = str(month)

if(month < 10):
    mm =  "0" + mm

targetUrl = baseUrl + yy + mm + "01"
print(targetUrl)

res = requests.get(targetUrl)
#print(res.text)
tt = res.text
j =  json.loads(tt)

for data in j["data"]:
    print(data[0])
