class A:
    
    def __init__(self):        
        print("init A")
        self.Name = "A"
        self.Local = "a"
        self.Counter = 0

    def __str__(self):
        return self.Name

    def get_counter(self):
        return self.Counter

    def Announcements(self):
        print("I'm AClass")

class B(A):
    mCustomName = ""

    def __init__(self, mValue):
        print("init B")
        super().__init__()
        self.Local = "b"
        self.mCustomName = mValue

    def Announcements(self):
        print("I'm BClass")
    
class C(B):
    def __init__(self):
        print("init C")
        
        #OK
        #super(C,self).__init__("my name C")

        #OK
        #B.__init__(self,"my name C")

        #OK
        super().__init__("my name C")

        self.Local = "c"

c = C()
print(c)
print(c.Local)
print(c.get_counter())
c.Announcements()
print(c.mCustomName)

b = B("my name B")
b.Announcements()
print(b.mCustomName)

a = A()
a.Announcements()