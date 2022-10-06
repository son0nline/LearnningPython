list1 = [1, 2, 3 , 4, 6]
list2 = [4, 5, 6, 7]
 
# Lists converted to sets
set1 = set(list2)
set2 = set(list1)

checkset = set1.intersection(set2)
print(checkset)

# & operation 

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)

mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)
