print("I'm {0} year{1} old".format(str(33),"s"))

print("[{1}] : [{0}] : [{1}] : [{2}] : [{0}] ".format("value 0","value 1","value 2"))


#string placeholder
for i in range(1,15):
    print("{0:2} squared is {1:4} and cubed is {2:<5}".format(i, i**2, i**3)) # **= i!x

for i in range(1,15):
    print("{2}{0}{1}".format("*"*i,"*"*(i-1)," "*(15-i)))
