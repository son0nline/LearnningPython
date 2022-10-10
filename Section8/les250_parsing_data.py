import os
with open('D:\\password-list-top-1-million.txt') as pass_info:
    lineIdx = 0
    for line in pass_info.readlines():
        lineIdx+=1
        if '0987654321' == line.rstrip():
            print("Found it in line",lineIdx)

with open('Section8\\country_info.txt') as country_info:
    country_info.readline() #skip first line
    for line in country_info.readlines():
        country,capital,cc,cc3,iac,timezone,currency = (line.split("|"))
        if country == 'Vietnam' or country == 'Japan':
            print(country,capital,cc,cc3,iac,timezone,currency, sep='\n\t')
        



