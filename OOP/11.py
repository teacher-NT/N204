import os
os.system("cls")

class Animal:
    def sound(self):
        print("Hayvon gapirmoqda")

class Begemot(Animal):
    pass

class Fil(Animal):
    def sound(self):
        print("Fil ovoz chiqardi...")


b1 = Begemot()
f1 = Fil()

b1.sound()
f1.sound()