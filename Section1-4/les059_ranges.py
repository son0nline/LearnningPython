for i in range(1,10): # from 1 to < 10
    print("i={}".format(i))
print("-"*20)
for i in range(10): # from 0 to < 10
    print("i={}".format(i))

print("-"*20)
for i in range(0,10,2):
    print("i={}".format(i))

print("-"*20)
for i in range(10,0,-2):
    print("i={}".format(i))

print("-"*20)
i = 4
if i in range(0,10):
    print("OK")



print("-"*20)
shop_list = ["milk","pasta","eggs","spam","bread","rice"]
find_item = shop_list[3]
found = None
for index in range(len(shop_list)):
    print(index)
    if shop_list[index] == find_item:
        print("found [{}] at {}".format(shop_list[index], index))
        found = index

if found is not None:
    print("found [{}] at {}".format(find_item, found))
else:
    print("not found") 

if find_item in shop_list:
    print("{} in {}".format(find_item,shop_list.index(find_item)))
