t = "a","b","c"
print(t)

g = t
print(id(t))
print(id(g))


print(t[0])
print(g[0])

tempT = list(t)
print(tempT)
tempT[0] = "d"
t = tuple(tempT)
print(t)

print(id(t))
print(id(g))

#unpack tuple
a, b, c = t
a = "ab"
print(a)
print(t)

# unpack list
ls = [1,2,3]
a,b,c = ls
print(a)