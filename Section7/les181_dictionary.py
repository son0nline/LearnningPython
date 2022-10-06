mDict = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : 3    
}

for item in mDict.items():
    key, value = item
    print(key, value, sep=', ')

for key in mDict.keys():
    print(key)

for value in mDict.values():    
    print(value)

def print_dict(mdict: dict):
    for item in mdict.items():
        key, value = item
        print(key, value, sep=', ')

print(mDict["key1"])
print(mDict.get("key2"))
print(mDict["key3"])

#print(mDict["key4"]) # error
print(mDict.get("key4")) # return None
print_dict(mDict)

#add new item to dict 
print("*" * 80)
mDict["newKey"] = "newValue"
print_dict(mDict)

# set default will create new item with value if not exist or get value if it was existed
a = mDict.setdefault("newKey2", "newValue2")
print("aaaaa",a)
b = mDict.setdefault("newKey2", "newKey2_update") # <- it's not update new value
print("bbbbb",b) # output still "newValue2"

#change item value 
print("*" * 80)
mDict["key3"] = 10
print_dict(mDict)

#remove item 
print("*" * 80)
del mDict["newKey"]
mDict.pop("key2")

# safe delete
#del mDict["notExistKey"] # raise KeyError
#mDict.pop("notExistKey") # raise KeyError
if mDict.get("notExistKey") != None:
    del mDict["notExistKey"]
print_dict(mDict)


#copy dict
newDict = mDict # not copy just create new cursor to mDict data
newDict["key1"] = "updated value"
print("*"*80)
print("copy dict")
print_dict(mDict)
print("*"*80)
print_dict(newDict)
print("*"*80)

# true copy
print("*"*80)
print("true copy")
newDict = mDict.copy()
newDict["key1"] = "updated"
print_dict(mDict)
print("*"*80)
print_dict(newDict)
print("*"*80)