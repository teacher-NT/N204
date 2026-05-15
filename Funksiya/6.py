import os
os.system("cls")


ages = [19,15,17,16,20,18]

# def func(n):
#     return n >= 18
# lst = list(filter(func, ages))
# print(lst)

lst = list(filter(lambda n: n>=18, ages))
print(lst)

# lst = []
# for i in ages:
#     if i >= 18:
#         lst.append(i)
# print(lst)