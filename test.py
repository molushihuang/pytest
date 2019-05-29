import math

x = [2, 4, 1, 9, 5, 6]


# x.sort()
# del x[0]
# print(x)
# print(sorted(x))

# if x[0] > 3:
#     print(x[0])
# elif x[1] > 2:
#     print(x[1])
# else:
#     print(x[3])

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# sum = 0
# for x in range(101):
#     sum = x + sum
#
# print(sum)


# L = ['Bart', 'Lisa', 'Adam']
# n = 0
# while n < 3:
#     print("hello," + L[n])
#     n = n + 1

def my_abs(number):
    if not isinstance(number,(int,float)):
        raise TypeError("bad operand type")
    if number >= 0:
        return number
    else:
        return -number


print(my_abs(-8))
