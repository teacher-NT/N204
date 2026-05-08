import os
os.system("cls")

# tuple1 = ('Salom', "Hello", 1,2,3)

# # tuple1[2] = "Nice"
# print(tuple1)
# print(tuple1[3])

# tuple1 = (1,2,4,0,3,8,5,7,6,9)
# # print(tuple1[15])
# print(tuple1[3:])
# print(tuple1[:5])
# print(tuple1[2:6])
# print(tuple1[1:8:2])
# print(tuple1[-2]) # orqadan keladi
# print(tuple1[::-1])


# fruits = ("apple",'banana','peach','melon','kivi')
# if "banana" in fruits:
#     print("Yes")
# else:
#     print("No")


# fruits = ("apple",'banana','peach','melon','kivi')

# for i in range(len(fruits)):
#     print(fruits[i])

# for i in fruits:
#     print(i)

# fruits = ("apple",'banana','peach','melon','kivi')
# fruits2 = ('pear', 'cherry', 'watermelon')

# fruits3 = fruits + fruits2
# print(fruits3)


tuple1 = (1,2,3,4,5,6,7,8,9)
# a = tuple1[0]
# b = tuple1[1]
# c = tuple1[2]
a,b,*c = tuple1
print(a,b,c)