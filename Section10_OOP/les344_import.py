from les344_module import *


print(normalVariable)
#private can't call
#print(_singleUnderscoreVariable)
#print(__doubleUnderscoreVariable__)
publicFunc()
#_privateFunc()

print("*"*80)
user = User()
print(user.normalVariable)
print(user._singleUnderscoreVariable)
print(user.__doubleUnderscoreVariable__)
print(user._privateVariable)
print(user.__privateVariable__)

print(user.name)
print(user.UserName)

user.publicFunc()
user._privateFunc()
user.staticFunc()
user.getPrivateVariable()


user._set__counter(12)
print(user.counter)
print(user._get__counter())

user.counter = 10
print(user.counter)
print(user._get__counter())