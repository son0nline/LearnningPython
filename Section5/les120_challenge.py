data = ""
lsNum = []
while data == "":
    data = input("Please enter three numbers:")
    lsStr = data.split(',')
    if len(lsStr) != 3:
        data = ""
        continue

    #print(lsStr)
    for str in lsStr:
        if not str.lstrip('+-').isnumeric():
            data = ""
            break
    
    if data == "":
        continue

    lsNum = [int(i) for i in lsStr]

a, b, c = lsNum
result = a + b - c
print(lsNum[0]+lsNum[1]-lsNum[2])
print(result)