nums = list(range(10))
even = nums[::2]
odd = nums[1::2]

nestLs = [odd,even]

print(nestLs)

for i in nestLs:
    print(i)
    for j in i:
        print(j)