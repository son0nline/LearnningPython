list1 = [1, 2, 3 , 4,5]
list2 = [4, 5, 6, 7]
 
# Lists converted to sets
set1 = set(list2)
set2 = set(list1)
 
# symmetric_difference method
newSet1 = set1.symmetric_difference(set2)
 
newSet2 = set2.symmetric_difference(set1)

newSet3 = set1 ^ set2

# Print the new set
print(newSet1)
print(newSet2)
print(newSet3)
 
