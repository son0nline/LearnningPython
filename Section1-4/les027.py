string1 = 'the name is "Mountant"'
print(string1)
print(string1[0])
print(string1[1])
print(string1[-1])


strPath = "e:\\nameofFolder"
print(strPath)
strPath2 = r"e:\nameofFolder"
print(strPath2)


# index 
strIndex = "0123456"
print(strIndex[0])
print(strIndex[6]) # 7 is out of index
print(strIndex[-1])
print(strIndex[-7])# -8 is out of index
# range 
print(strIndex[0:3]) # start at 0 and end before 3
print(strIndex[:3]) # start of array to before 3
print(strIndex[3:]) # start at 3 to end of array
print(strIndex[2:4]) # start at 2 and end before 4