
import json
import urllib.request

urlSource = "https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json"
with urllib.request.urlopen(urlSource) as jsonStreamData:
    dataStream = jsonStreamData.read().decode('utf-8')
    data = json.loads(dataStream)

print(type(data))
for key in data:
    print(key)

description = data["description"]
print(description)

for year, value in data["data"].items():
    print(year, value)

    