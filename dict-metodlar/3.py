
import os
os.system("cls")

# car = {
#     "brand": "BMW",
#     "model": "M5 F90 Competition",
#     "price": 128000,
#     "color": "green",
#     "year": 2023
# }
# car['country'] = "Germany"

# for i in car:
#     print(i, car[i])


car2  ={
    "brand": input("brand: "),
    "model": input("model: "),
    "price": int(input("price: ")),
    "color": input("color: ")
}
print("= "*15)
for i in car2:
    print(i, car2[i])