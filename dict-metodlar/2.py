import os
os.system("cls")

car = {
    "brand": "BMW",
    "model": "M5 F90 Competition",
    "price": 128000,
    "color": "GREEN",
    "year": 2023
}
car['country'] = "Germany"

if "color" in car:
    if car['color'].lower() == 'Green'.lower():
        print('green Yes')
    print("Yes")
else:
    print("No")