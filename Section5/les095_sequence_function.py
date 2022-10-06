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


odd = nummeric[::2]
even = nummeric[1::2]
print(odd)
print(even)


print(min(odd))
print(max(odd))
print(sum(odd))

print(min(even))
print(max(even))
print(sum(even))