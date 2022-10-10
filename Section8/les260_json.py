import json

# languages = [
#     ['ABC', 1987],
#     ['Algol 68', 1968],
#     ['APL', 1962],
#     ['C', 1973],
#     ['Haskell', 1990],
#     ['Modula-2', 1987],
#     ['Perl', 1987],
# ]

languages = {
    'ABC':1987,
    'Algol 68':1968,
    'APL':1962,
    'C':1973,
    'Haskell':1990,
    'Modula-2':1987,
    'Perl':1987,
}

if 0:
    with open('Section8\\les260json.json','w+', encoding="utf-8" ) as jsonFile:
        json.dump(languages, jsonFile)
else:
    with open('Section8\\les260json.json', 'r', encoding="utf-8" ) as jsonFile:
        data = json.load(jsonFile)
    
    print( type(data))
    for key in data:
        print(key,data[key])