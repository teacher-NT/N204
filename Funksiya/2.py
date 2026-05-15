import os
os.system("cls")

def salom_ber():
    print("Hello everyone!!!")
    print("Hello everyone!!!")

def func1():
    pass

def add(a, b):
    print(a+b)

# add(4,5)
# add("Salom ", "Dunyo")

def add2(a: int, b: int):
    print(a+b)


def add3(a:int, b:int):
    """
        Bu funsksiya 2 ta sonning yig'indi, ko'paytma va 
        darajasini hisoblaydi
    """
    return a+b, a*b, a**b

n = add3(3,4)
# print(n)


def add4(a:int, b:int) -> int:
    return a+b
print(add4(4,5))
