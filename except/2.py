import os
os.system("cls")

try:
    a = int(input("Son kiriting: "))
    b = int(input("Son kiriting: "))
    print(a+b)
except:
    print("Xatolik sodir bo'ldi!")
else:
    print("Try muvafaqqiyatli bajarildi!")