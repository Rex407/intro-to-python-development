import math

list1 = [5,10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

t = input("What is the temperature?: ")
sign = t[-1]
t = int(t[:-1])
if sign == "C" or sign == "c":
    t = round(t * (9/5) + 32)
    print(str(t) + 'F')

elif sign == "F" or sign == 'f':
    t = round((t-32) * (5/9))
    print(str(t) + 'C')


