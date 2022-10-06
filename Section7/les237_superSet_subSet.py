list1 = [1, 2, 3 , 4, 5]
list2 = [4, 5]
list3 = [4, 5, 6]
 
# Lists converted to sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
 
# symmetric_difference method
check1 = set1.issuperset(set2)
check2 = set2.issubset(set1)
print(check1,check2)

check3 = set3.issubset(set1)
print(check3)

# operation 

print(set1 > set2) 
print(set1 >= set2)
print(set2 < set1)  
print(set2 == set([4, 5]))
# false
print(set1 > set3) 
print(set1 >= set3) 
