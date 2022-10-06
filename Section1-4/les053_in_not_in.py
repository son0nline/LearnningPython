strString = 'Udemy Learn Python Programming Masterclass'

#letter = input('input your letter:')
letter = 'udemy'
if  letter in strString.casefold():
    print(f'[{letter}] is in [{strString.casefold()}]')


if  letter not in strString:
    print(f'[{letter}] is not in [{strString}]')


lsInt = [1,2,3,4,5,6]
lsSInt = [2,3]
i = 4
if i in lsInt:
    print(f'{i} int lsInt')

if lsSInt in lsInt: # can't find
    print('lsSInt in lsInt')