class Student:
    ism = "Alisher"
    familya = "Abdullayev"
    manzil = "Toshkent"
    yosh = 42

# print(ism)
s1 = Student()
s1.baho = 3
s1.ism = "Bobur"
print(s1.ism)
print(s1.baho)

s1.manzil += " shahar, Uchtepa"
print(s1.manzil)

a = 12
b = 3.5
c = "hello"
d = [1,2,3]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(s1))