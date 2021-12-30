import json
with open("config.json",mode="r") as file:
    data = json.load(file)
print(data)
print(data["name"])
print(data["version"])