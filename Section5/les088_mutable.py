lsOptions = ["Learn python","Fix Ds bug","Learn Android"]
lsOptions2 = lsOptions

print(id(lsOptions))
print(id(lsOptions2))

lsOptions.append("out ds")

lsOptions2 += ["support to end VFM then out"]

print(id(lsOptions))
print(id(lsOptions2))

print(lsOptions2)