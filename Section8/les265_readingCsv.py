import csv

filename = 'Section8\\OlympicMedals_2020.csv'


with open(filename, 'r', encoding="utf-8" , newline=''  ) as csvFile:
    headers = csvFile.readline().strip().split(',')
    print(headers)
    
    datareader = csv.reader(csvFile)
    for row in datareader:
        print(row)

print("*"*80)
filename = 'Section8\\cereal_grains.csv'
with open(filename, 'r', encoding="utf-8" , newline=''  ) as csvFile:
    headers = csvFile.readline().strip().split(',')
    print(headers)
    
    datareader = csv.reader(csvFile, quoting=csv.QUOTE_NONNUMERIC)
    for row in datareader:
        print(row)

print("*"*80)
filename = 'Section8\\address.csv'
with open(filename, 'rt', encoding="utf-8" , newline=''  ) as csvFile:
    headers = csvFile.readline().strip().split(',')
    print(headers)
    
    datareader = csv.reader(csvFile, skipinitialspace=True
        #, quotechar="\""    # hai cai nay dung thay cho nhau duoc
        , doublequote=True   # hai cai nay dung thay cho nhau duoc
    )
    for row in datareader:
        print(row)


print("*"*80)
filename = 'Section8\\country_info.txt'
with open(filename, 'rt', encoding="utf-8" , newline=''  ) as csvFile:
    datareader = csv.reader(csvFile,delimiter='|')
    for row in datareader:
        print(row)
        
print("*"*80)
filename = 'Section8\\country_info.txt'
with open(filename, 'rt', encoding="utf-8" , newline=''  ) as csvFile:
    sample = csvFile.read()
    country_dialect = csv.Sniffer().sniff(sample)
    csvFile.seek(0)
    datareader = csv.reader(csvFile, dialect=country_dialect)
    for row in datareader:
        print(row)