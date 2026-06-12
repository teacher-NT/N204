import os
os.system("cls")

class Person:
    def __init__(self, i, y, m):
        self.ism = i
        self.yosh = y
        self.manzil = m

    def __gt__(self, n):
        return self.yosh > n
    

class Worker:
    def __init__(self,i,y,m,l,maosh):
        self.ism = i
        self.yosh = y
        self.manzil = m
        self.lavozim = l
        self.maosh = maosh
    
    def __gt__(self, n):
        return self.maosh > n

w1 = Worker("Husan", 22, "Samarqand", "Manager", 500)
print(w1 > 100)

p1 = Person('Saidaloxon', 15, "Toshkent")
print(p1 > 18)
