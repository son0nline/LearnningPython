age = 33
name = "Mountant"


print(f"I'm {age} years old :D") # like $"{variable}" in c#
print(f"10/3 = [{(10/3):10.3f}]") # placeholder 10 space and have 3 digit after [.]

print("I'm %s" % name)
print("I'm %s %d years old. I know 10/3=[%f]" % (name,age,(10/3)))
print("10/3=[%10.3f]" % (10/3))

