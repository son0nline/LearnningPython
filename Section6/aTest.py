def multiply(x, y):
    """
    Multiply 2 numbers.
 
    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.
 
    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result

def fizz_buzz(n:int)->str:
    """
    fizz_buzz game
    :param n: The number to get fizz_buzz.
    :return: string.
    """
    if n % 5 == 0 and n % 3 == 0:
        return "fizz buzz"

    if n % 5 == 0:
        return "buzz"

    if n % 3 == 0:
        return "fizz"
    
    return str(n)
    

def get_integer(promt:str)->int:
    """
    Get a integer from standard input
    :param promt: show promt
    :return: integer
    """
    while True:
        temp = input(promt)
        if temp.lstrip('-').isnumeric():
            return int(temp)
        print(f"[{temp}] is not a number")


print(get_integer.__doc__)
print("_" * 1)
help(get_integer)

a = multiply(2,4)
char = 'a'
if char.isalnum(): #alpha numberic string [A-Za-z0-9]
    print(a)

for i in range(100):    
    print(i ," ", fizz_buzz(i))

def factorial(n:int):
    """
    Docstring
    :param n: The number to get factorial.
    :return: factorial.
    """
    if n == 0:
        return 1
    return n * factorial(n-1)


for i in range(36):    
    print(i ," ", factorial(i))


def sum_numbers(*arg:int)->float:
    """
    sum_numbers
    :param arg: int list
    :return : integer sum or all argument
    """
    rs = 0
    for i in arg:
        rs += i
    return rs

print(sum_numbers(1.1,10.5,2.5))