import os
os.system("cls")

def sum_even(tuple1):
    if len(tuple1) == 0:
        return 0
    n = tuple1[0]
    if n % 2 == 0:
        return n + sum_even(tuple1[1:])
    return sum_even(tuple1[1:])

print(sum_even((2,3,5,6,3,7,8,4)))