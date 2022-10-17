import traceback

def IWillErr():
    return 1/0

def factorical(n):
    if n <= 1:
        return 1
    else:
        return n * factorical(n-1)



try:
    IWillErr()
    print("hi")
except ZeroDivisionError as e:
    print("ZeroDivisionError")
    print(e)
    traceback.print_exc()
except Exception as e: 
    print(e)
except:
    print("System error!!!")
    traceback.print_exc()


try:
    print(factorical(998))    
except ( RecursionError,Exception) as e: 
    print(e)
except:
    print("System error!!!")
    traceback.print_exc()
finally:
    print("done")