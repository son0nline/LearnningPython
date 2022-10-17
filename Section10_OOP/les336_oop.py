from datetime import date

current_year = date.today().year
print(current_year)

a = 1
b = 2 
print(a.__add__(b))
print(a)

class User:

    yearOfBirth = 0

    def __init__(self, usname:str, passwd:str ) -> None:
        # public properties
        self.UserName = usname
        self.PassWd = passwd
        self.warning = 0

    
    def Authenticate(self, usname:str, passwd:str ) -> bool:
        return self.UserName == usname and self.PassWd == passwd

    def IncreaseWarning(self) -> int:
        self.warning += 1
        return self.warning

    def GetYearsOld(self) -> int:
        return date.today().year - self.yearOfBirth
            
us = User("usname", "*******")
print(us, type(us))
print(us.UserName)
print(us.Authenticate("a","b"))
print(us.IncreaseWarning(),us.IncreaseWarning(),us.IncreaseWarning())

us.yearOfBirth = 1989
print(us.GetYearsOld())

print(us.__dict__)