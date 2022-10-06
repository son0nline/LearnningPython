nummeric = list(range(1,10)) #[1,2,3,4,5,6,7,8,9]
odd = nummeric[::2]
even = nummeric[1::2]
print(odd)
print(even)


print(min(odd))
print(max(odd))

print(min(even))
print(max(even))

newLs = nummeric[::2]
newLs.extend(even)

print(odd)
print(even)
print(newLs)

newLs.sort()
print(newLs)

newLs.sort(reverse=True)
print(newLs)

print("*"*80)
del newLs[5::]
newLs.remove(6)
print(newLs)

print("*"*80)

rndLs = [7, 10, 8, 6, 1, 2, 6, 2, 4, 6, 10, 5, 9, 10, 4, 3, 2, 1, 8, 6, 10, 5, 1, 2, 10, 6, 3, 8, 8, 8, 2, 4, 8, 3, 5, 7, 1, 4, 9, 5, 2, 5, 4, 8, 1, 3, 4, 7, 9, 3, 2, 2, 2, 4, 3, 10, 7, 7, 4, 6, 6, 7, 8, 6, 5, 5, 6, 3, 9, 10, 7, 5, 8, 9, 5, 1, 7, 10, 9, 4, 3, 6, 3, 2, 10, 10, 8, 5, 10, 2, 5, 6, 1, 1, 5, 7, 10, 7, 6, 10]

for i in range(11):
    print("[{}] appeared {} times".format(i, rndLs.count(i)))


quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
print(len(rndLs))
print(quote.count("ion"))



data = "1234567890"

nummeric = [int(char) for char in data]

stringLs = list(data)
nummericLs = list(nummeric)
copyNummericLs = nummericLs.copy()


print(stringLs)
print(nummericLs)
print(copyNummericLs)

print(id(nummericLs))
print(id(copyNummericLs))
