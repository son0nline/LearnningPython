bTest = True
bTest2 = bTest
print(id(bTest))
print(id(bTest2))
bTest = False
print(id(bTest))
print(id(bTest2))