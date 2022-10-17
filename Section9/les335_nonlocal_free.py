def func1():
    def func2():
        def func3():
            #print(locals())
            z = "func3" + y + x          
            return z
        #print(locals())
        y = "func2" # + func3() # sẽ lỗi vì func3 gọi đến y nhưng y chưa được assign giá trị trước khi gọi func3()
        y += func3() 
        return y
    #print(locals())
    #x = 'func1' + func2() # sẽ lỗi vì x chưa được asign giá trị trước khi gọi func2()
    x = 'func1' 
    x += func2()
    return x

#print(locals())
print(func1())
#print(x) #NameError: name 'x' is not defined

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"

  def myfunc3():
    x = "myfunc3"

  myfunc2()
  myfunc3()
  return x

print(myfunc1())
