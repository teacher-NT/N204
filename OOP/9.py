import os
os.system("cls")


class School:
    def __init__(self, m, n, r, t):
        self.manzil = m
        self.soni = n
        self.raqam = r
        self.til = t
    
    def __str__(self):
        return f"{self.manzil} {self.soni} {self.raqam} {self.til}"
    
    def __gt__(self, n):
        print("Katta operatori")
        return self.soni > n
    
    def __lt__(self, n):
        return self.soni < n

    def __eq__(self, n):
        return self.soni == n
    
    def __add__(self, n):
        self.soni += n

    def __sub__(self, n):
        self.soni -= n

    def __mul__(self, n):
        self.raqam *= n

    def __truediv__(self, n):
        self.raqam /= n
    
s1 = School("Chilonzor", 2000, 78, "O'zbek tili")
# print(s1 > 5000)
# print(s1 < 500, s1.soni < 500)
# print(s1 == 2000)

s1 + 100
s1 - 2000
s1 * 2
s1 / 3
print(s1)