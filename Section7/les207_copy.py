import copy


mDict1 = {  "1": "computer",
            "2": "monitor",
            "3": ["1","2","3"],
        }

# shallow copy
#mDict2 = mDict1.copy()

# deep copy
# create new object absolute different with source object
mDict2 = copy.deepcopy(mDict1)

# add value
mDict1["4"] = "keyboard" # with shallow copy it will not append to mDict2
mDict2["3"].append("4") # with shallow copy it will append to both mDict1 mDict2

print(mDict1)
print(mDict2)