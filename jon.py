import json
data = {
    "udi": "28487678947878"
}
data = json.dumps(data)
print(data)
with open('conf.json', mode='r') as confe:
    print(confe.read())
    d = json.loads(confe.readline().encoding='utf-8')
    print(d)
