list1 = [1, 2, 3 , 4]
list2 = [4, 5, 6, 7]
 
# Lists converted to sets
set1 = set(list2)
set2 = set(list1)
 
# Update method
newSet1 = set1.union(set2)
 
newSet2 = set2.union(set1)

newSet3 = set1 | set2

# Print the updated set
print(set1)
print(newSet1)
print(newSet2)
print(newSet3)
 
