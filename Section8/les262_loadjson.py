import json

with open('Section8\\temperature_anomaly.json', 'r', encoding="utf-8" ) as jsonFile:
    data = json.load(jsonFile)

print(type(data))
for key in data:
    print(key)

description = data["description"]
print(description)

for year, value in data["data"].items():
    print(year, value)

    