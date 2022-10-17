import random

class User:
    #everything is public

    def __init__(self) -> None:
        self._counter = 0
    
    def _get__counter(self):
        return self._counter
    def _set__counter(self, counter):
        self._counter = counter
    
    # thực ra tính năng hơi thừa vì nó public mẹ hết rồi
    counter = property(_get__counter,_set__counter)

user = User()

user._set__counter(12)
print(user.counter)
print(user._get__counter())

user.counter = 10
print(user.counter)
print(user._get__counter())

user.counter += 1
print(user.counter)
print(user._get__counter())

print(user._counter)