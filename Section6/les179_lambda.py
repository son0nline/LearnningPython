
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



a = 1
b = 2
rs =  a if a==1 else b # tenary toán tử 3 ngôi

def double(x):
    return x * 2

x2 = lambda x: x * 2

sequence = [2,4,7,9,3]
print(sequence)
doubled = [double(x) for x in sequence]
print(doubled)

mapdoubled = map(double,sequence)
for m in mapdoubled:
    print(m)


print(list(map(x2,sequence)))