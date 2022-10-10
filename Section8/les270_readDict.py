import csv

print("*"*80)
filename = 'Section8\\OlympicMedals_2020.csv'

with open(filename, 'rt', encoding="utf-8" , newline=''  ) as csvFile:
    datareader = csv.DictReader(csvFile)
    for row in datareader:        
        print(type(row), row)

print(datareader)