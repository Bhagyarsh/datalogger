import random
import requests
import json


def getrandint():
    return(random.randint(0, 9))


for i in range(0, 14):
    uid += str(getrandint())
uid = "28487678947878"
url = 'http://solar.bhkdev.tk/api/datalogger/check?uvid='+uid

API_ENDPOINT = 'http://solar.bhkdev.tk/api/datalogger/check?uvid=12345678901234'
print(uid)
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "47269bb7-0ad2-f82e-5c6e-9f3e8ba9d8b9"
}
r = requests.get(url=url, headers=headers)

data = r.content.decode('utf-8')
url = 'http://solar.bhkdev.tk/api/datalogger/add'
print(data)
if data == '0':
    print(data)
    uid = {"uvid": uid}
    print(uid)
    r = requests.post(url=url, data=json.dumps(uid), headers=headers)
    print(r.content)

# extracting response text
