import json

with open('config.json') as file:
    data = json.load(file)
#print(type(data))
print("name",data['name']) #印出name 的資料
print("version",data['version'])#印出 version 的資料


