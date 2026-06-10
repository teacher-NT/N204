import os
os.system("cls")

class A:
    def func1(self):
        print("A class")

class B:
    def func1(self):
        print("B class")

class C(A):
    pass

class D(C, B):
    pass

class E(C, D):
    pass

e1 = E()
e1.func1()

# d1 = D()
# d1.func1()
# print(D.__mro__)