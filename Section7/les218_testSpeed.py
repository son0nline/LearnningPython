import random
import time

maxValue = 40000000 #40M

rnd = random.randint(1,maxValue)


lList = list(range(maxValue))
start_time = time.time()
if rnd in lList:
    print("ok")
print("--- {0:20} seconds ---".format((time.time() - start_time)))
lList.clear()
lList = None

sSet =  set(range(maxValue))
start_time = time.time()
if rnd in sSet:
    print("ok")
print("--- {0:20} seconds ---".format((time.time() - start_time)))
sSet.clear()
sSet = None


# test remove duplicate in list
# original = ["a","b","c","a"]
# unique = []
# [unique.append(n) for n in original if n not in unique] # this syntax 😣
# print(unique)

# print([n for n in original if n == "a"])