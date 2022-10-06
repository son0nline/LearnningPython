# set is unique list items
# set is not order  -- vì không có order nên không gọi theo kiểu index được ex:(set[index])
# set nhanh hơn (nhưng tốn ram hơn thì phải 😁 trong testSpeed không tạo được 50M items)

mSet = {"a","b","c","a"}
print(mSet) # {'a', 'c', 'b'} or {'c', 'b','a'}
for i in mSet:
    print(i)

var = mSet.pop()
print("pop1",var)
var = mSet.pop()
print("pop2",var)

print(mSet) 

print("remove", "*"* 30) 
mSet = {"a","b","c","a"}
mSet.remove("a") # error if not exist
mSet.discard("a") #safe remove
print(mSet) 
print("end", "*"* 30) 



