import os
os.system("cls")

# with open("N204/fayl/test3.txt", "w") as file:
#     names = ['Saidaloxon', 'Muahmmadsodiq', 'Azizullo', 'Saidakbar','Husan', 'Abdullo']
#     names = list(map(lambda n: n+"\n", names))
#     file.writelines(names)


with open("N204/fayl/test3.txt", "w") as file:
    names = ['Saidaloxon',66, 'Muahmmadsodiq', 'Azizullo',16, 'Saidakbar','Husan',12, 'Abdullo']
    names = list(map(lambda n: str(n)+"\n", names))
    file.writelines(names)

