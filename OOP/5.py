import os
os.system("cls")

class Uchar:
    def uchmoq(self):
        print("Uchmoqda...")

class Suzuvchi:
    def suzmoq(self):
        print("Suzmoqda...")
    
class Ordak(Uchar, Suzuvchi):
    pass

ordak1 = Ordak()
ordak1.uchmoq()
ordak1.suzmoq()
