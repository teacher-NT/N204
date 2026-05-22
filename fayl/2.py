import os 
os.system("cls")

# with open("N204/fayl/test.txt") as file:
#     matn = file.read(10)
#     print(matn)


# with open("N204/fayl/test.txt") as file:
#     matn = file.readline()
#     print(matn)
#     matn = file.readline()
#     print(matn)

with open("N204/fayl/test.txt") as file:
    matn = file.readlines()
    print(matn)

