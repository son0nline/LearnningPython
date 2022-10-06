list1 = [1, 2, 3 , 4, 6]
list2 = [4, 5, 6, 7]
 
# Lists converted to sets
set1 = set(list2)
set2 = set(list1)

checkset1vsset2 = set1.difference(set2)
checkset2vsset1 = set2.difference(set1)

print(checkset1vsset2)
print(checkset2vsset1)


# - operation 
print( set1 - set2)
print( set2 - set1)