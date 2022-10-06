import re


def fibonacci(n:int)->int:
    if n == 0 or n == 1:
        return n

    result = None
    n1, n2 = 0, 1

    for i in range(n-1):
        result = n1 + n2
        n1, n2 = n2, result
    return result

for i in range(30):
    print(i ," : ", fibonacci(i))

