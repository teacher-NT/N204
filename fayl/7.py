import os
os.system("cls")

with open("image.jpeg", "rb") as file:
    pixels = file.read()
    # for i in pixels:
    #     print(i, end=" ")
    # print(len(pixels))

with open("nusxa.jpeg", "wb") as file:
    file.write(pixels)
    print("Fayl nusxalandi...")