age = int(input('How old are you?'))

if 13 <= age <= 19:
    print('you are teenage')
elif age < 13:
    print('a good child')
else:
    print('an old man waiting for die alone')


bHaveJob = True

if not bHaveJob:
    print("poor")
else:
    print('have a good day at work!')