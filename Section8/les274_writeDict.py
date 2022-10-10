import csv

headers = ['Rank','Country','Gold','Silver','Bronze','Total']

data = [
{'Rank': '83', 'Country': 'Kazakhstan', 'Gold': '0', 'Silver': '0', 'Bronze': '8', 'Total': '8'}
,{'Rank': '84', 'Country': 'Mexico', 'Gold': '0', 'Silver': '0', 'Bronze': '4', 'Total': '4'}
,{'Rank': '85', 'Country': 'Finland', 'Gold': '0', 'Silver': '0', 'Bronze': '2', 'Total': '2'}
,{'Rank': '86', 'Country': 'Botswana', 'Gold': '0', 'Silver': '0', 'Bronze': '1', 'Total': '1'}
,{'Rank': '86', 'Country': 'Burkina Faso', 'Gold': '0', 'Silver': '0', 'Bronze': '1', 'Total': '1'}
,{'Rank': '86', 'Country': "Côte d'Ivoire", 'Gold': '0', 'Silver': '0', 'Bronze': '1', 'Total': '1'}
,{'Rank': '86', 'Country': 'Ghana', 'Gold': '0', 'Silver': '0', 'Bronze': '1', 'Total': '1'}
,{'Rank': '86', 'Country': 'Grenada', 'Gold': '0', 'Silver': '0', 'Bronze': '1', 'Total': '1'}
,{'Rank': '86', 'Country': 'Kuwait', 'Gold': '0', 'Silver': '0', 'Bronze': '1', 'Total': '1'}
,{'Rank': '86', 'Country': 'Moldova', 'Gold': '0', 'Silver': '0', 'Bronze': '1', 'Total': '1'}
,{'Rank': '86', 'Country': 'Syria', 'Gold': '0', 'Silver': '0', 'Bronze': '1', 'Total': '1'}
    ]

fileName = "Section8\\mfile.csv"
with open(fileName,'w',encoding='utf-8',newline='') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
