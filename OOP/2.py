class Student:
    ism = "Alisher"
    familya = "Abdullayev"
    manzil = "Toshkent"
    yosh = 42

    def print_class(self):
        print(f"{self.ism} {self.familya} {self.manzil} {self.yosh}")

    def change_yosh(self, n):
        self.yosh += n

# print(ism)
s1 = Student()
s1.change_yosh(3)
s1.print_class()

s2 = Student()
s2.print_class()
