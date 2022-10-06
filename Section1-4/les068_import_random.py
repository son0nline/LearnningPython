import random

ls = []
while len(ls) < 100:
    ls.append(random.randint(1,10))

print(ls)

print("*"*80)
print(r"Vịt lost")

vitLost = []
while len(vitLost) <6:
    rnd = random.randint(1,55)
    if rnd not in vitLost:
        vitLost.append(rnd)

vitLost.sort()
print(vitLost)
