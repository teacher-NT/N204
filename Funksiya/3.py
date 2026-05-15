import os
os.system("cls")

def add(*a):
    print(a)
    print(sum(a))

# add(3,5,4,6,3,5)

def func1(**param):
    print(param)

# func1(ism='Alisher', yosh=19, manzil='Toshkent')


def func2(a,b,c=0):
    print(a+b+c)

func2(4,5)
func2(4,5,6)