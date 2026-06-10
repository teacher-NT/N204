import os
os.system("cls")

class Hayvon:
    def __init__(self, i, t, y):
        self.ism = i
        self.tur = t
        self.yosh = y

    def yurmoq(self):
        print("Hayvon yurmoqda...")

class Mushuk(Hayvon):
    def ovoz(self):
        print("Mushuk qo'shiq aytyapti...")

class Bori(Hayvon):
    def pishirmoq(self):
        print("Bo'ri ovqat pishirmoqda...")

m1 = Mushuk('Garfild', 'sut emizuvchi', 2)
b1 = Bori('Aleks', 'sut emizuvchi', 5)

m1.yurmoq()
m1.ovoz()
b1.yurmoq()
b1.pishirmoq()