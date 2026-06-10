import os
os.system("cls")

class Animal:
    def __init__(self, n, t, y):
        self.nom = n
        self.tur = t
        self.yosh = y

    def sound(self):
        print("Hayvon gapirmoqda...")

class Dog(Animal):
    def run(self):
        print("Dog is running...")

dog1 = Dog("Reks", "Sut emizuvchi", 9)

print(dog1.nom, dog1.tur, dog1.yosh)
dog1.sound()
dog1.run()