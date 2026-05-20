
import random as rd

print(rd.randint(1,100))

print(rd.uniform(1,10))

names = ['Saidaloxon', 'Azizullo', 'Nazirjon', 'Husan']
name = rd.choice(names)
# print(name)

print(rd.choices(names, k=2))

print(rd.sample(names, k=2))

rd.shuffle(names)
print(names)