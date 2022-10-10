import csv

print("*"*80)
filename = 'Section8\\country_info.txt'
with open(filename, 'rt', encoding="utf-8" , newline=''  ) as csvFile:
    
    # learning file struct
    sample = csvFile.read()
    for i in range(3):
        sample += csvFile.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    #country_dialect.skipinitialspace = True
    csvFile.seek(0)

    datareader = csv.reader(csvFile, dialect=country_dialect)
    for row in datareader:
        print(row)

print('*' * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    print(f'{attribute}: {getattr(country_dialect, attribute)} {repr(getattr(country_dialect, attribute))}')