import random



lsInt = []
#lsInt = [4, 19, 21, 26, 50, 51]
while len(lsInt) < 6:
    rnd = random.randint(1,55)
    if rnd not in lsInt:
        lsInt.append(rnd)
lsInt.sort()
print(lsInt)

for i in lsInt:
    if i == 22:
        print("not ok")
        break
else: #amazin! this is [else] of for not if
    # else fire when don't match any if condition
    print("ok")

print("*"*80)
guess_times = 0
while guess_times <= 6:
    guess_times = guess_times+1
    guess = random.randint(1,55)
    if guess in lsInt:
        print("Congratulation value is {}".format(guess))
        break;
else: # else fire when don't match any if condition
    print("Game Over!") 

