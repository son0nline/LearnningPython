import random
import time

maxValue = 30000000 #30M

rnd = random.randint(1,maxValue)


lList = list(range(maxValue))
start_time = time.time()
if rnd in lList:
    print("ok")
print("--- %s seconds ---" % (time.time() - start_time))
lList.clear()
lList = None

sSet =  set(range(maxValue))
start_time = time.time()
if rnd in sSet:
    print("ok")
print("--- %s seconds ---" % (time.time() - start_time))
sSet.clear()
sSet = None