i = 0
while i < 10:
    i+=1
    print(i)

print("*"*20)

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for i in range(0, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)