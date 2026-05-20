import os
os.system("cls")

try:
    a = int(input("Son kiriting: "))
    b = int(input("Son kiriting: "))
    print(a/b)
except ValueError:
    print("Kiritilgan qiymat son emas!")
except ZeroDivisionError:
    print("Sonni nolga bo'lib bo'lmaydi")
else:
    print("Try muvafaqqiyatli bajarildi!")

# a = int(input("Son kiriting: "))
# b = int(input("Son kiriting: "))
# print(a/b)