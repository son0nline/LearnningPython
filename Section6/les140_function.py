from re import I


def fncPrint(input='default value'):
    print(input)

def fnc_multiply(a,b):
    return a*b*1.0

def fnc_add(a: int, b:int)->int:
    return a+b


def fnc_listadd(ls: list):
    ls.append(len(ls))

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


print(fnc_add(3,5))
print(fnc_multiply(3,5))

fncPrint("hello")
fncPrint()

ls = []
fnc_listadd(ls)
fnc_listadd(ls)
print(ls)

a = get_integer(r"Nhập 1 số nguyên bất kỳ: ")

def sum_eo(n,t):
    if t not in "eo":
        return -1
    rs = 0
    for i in range(n,0,-1):
        if i % 2 == 0:
            rs += i
    return rs

sum_eo(10, 'e')


    