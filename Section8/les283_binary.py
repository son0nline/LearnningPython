#equation = bytes((207,128,114,194,178))
equation = b'\xcf\x80r\xc2\xb2'
print(equation) # output b'\xcf\x80r\xc2\xb2'
print(type(equation))
print(len(equation))
for byte in equation:
    print(byte,end=', ')
print()
print(equation.decode('utf-8'))
