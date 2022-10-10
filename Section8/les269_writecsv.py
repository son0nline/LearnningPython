import csv

headers = ['Country', 'Capital', 'CC', 'CC3', 'IAC', 'TimeZone', 'Currency']

data = [
    ['Vietnam', 'Hanoi', 'VN', 'VNM', '+84', 'UTC+07:00', 'Vietnamese đồng']
    ,['Virgin Islands', 'Road Town', 'VG', 'VGB', '+1 284', 'UTC-04', 'British Virgin Islands dollar']
    ,['Virgin Islands of the United States', 'Charlotte Amalie', 'VI', 'VIR', '+1 340', 'UTC-04', 'United States dollar']
    ,['Wallis and Futuna', 'Mata-Utu', 'WF', 'WLF', '+681', 'UTC+12:00', 'CFP franc']
    ,['Western Sahara', 'Laâyoune, (El Aaiún)', 'EH', 'ESH', '+212 5288/5289', 'UTC+01', 'Moroccan dirham']
    ,['Yemen', 'Sanaá', 'YE', 'YEM', '+967', 'UTC+03:00', 'Yemeni rial']
    ,['Zambia', 'Lusaka', 'ZM', 'ZMB', '+260', 'UTC+02:00', 'Zambian kwacha']
    ,['Zimbabwe', 'Harare', 'ZW', 'ZWE', '+263', 'UTC+02:00', 'Botswana pula']
    ]

fileName = "Section8\\mfile.csv"
with open(fileName,'w',encoding='utf-8',newline='') as csvFile:
    writer = csv.writer(csvFile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(headers)
    writer.writerows(data)
