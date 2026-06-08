class Student:
    def __init__(self, i, f, m, y):
        self.ism = i
        self.familya = f
        self.manzil = m
        self.yosh = y

    def print_class(self):
        print(f"{self.ism} {self.familya} {self.manzil} {self.yosh}")

    def change_yosh(self, n):
        self.yosh += n

    def change_name(self, new):
        self.ism += new
        self.ism = self.ism.upper()

# print(ism)
s1 = Student("Abdullo", 'Jalilov', "Buxoro", 18)
# s1.change_yosh(3)
s1.print_class()

s2 = Student("Saidakbar", "Qosimov", "Dombirobod", 16)
# s2.change_name(" Navoiy")
s2.print_class()
