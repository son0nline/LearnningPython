
#public 
normalVariable = 1
#private in module
_singleUnderscoreVariable = 1
__doubleUnderscoreVariable__ = 1

def publicFunc():
    print("I'm a public function")

def _privateFunc():
    print("I'm not a public function")
    print("I'm private")

#In Python, there is no existence of “Private” instance variables
# python class đếu có biến private
# tự mà ngầm hiểu thôi 
class User:
    #everything is public 
    normalVariable = 1    
    _singleUnderscoreVariable = 2
    __doubleUnderscoreVariable__ = 3

    def __init__(self) -> None:
        print("run in init")
        self._privateVariable = 4
        self.__privateVariable__ = 5
        self.name = "User Name"

    def publicFunc(self):
        print("I'm a public function")

    def _privateFunc(self):
        print("I'm not a public function")
        print("I'm private")

    @staticmethod
    def staticFunc():
        print("I'm staticmethod")

    def getPrivateVariable(self):
        print(self._privateVariable)

    def getName(self):
        return self.name    
    UserName = property(getName)
    
    _counter = 0
    def _get__counter(self):
        return self._counter
    def _set__counter(self, counter):
        self._counter = counter
    counter = property(_get__counter,_set__counter)

# không tự chạy khi bị import
if __name__ == "__main__":
    _privateFunc()