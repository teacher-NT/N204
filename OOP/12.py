import os
os.system("cls")

class BankAccount:
    def __init__(self, n, b):
        self.name = n
        self.__balans = b
    
    def get_balans(self, parol):
        if parol == 'qwerty':
            print(self.__balans)
        else:
            print("Parol xato.")
    
    def hisob_yangilash(self, parol, yangi):
        if parol == '1122':
            self.__balans += yangi
            print("Balans o'zgardi")
        else:
            print("Parol xato") 

b1 = BankAccount("Husan", 12000)
print(b1.name)
# b1.get_balans("12345678")
# b1.get_balans("qwerty")
# print(b1.__balans)

b1.hisob_yangilash("1122", 5000)
b1.get_balans("qwerty")