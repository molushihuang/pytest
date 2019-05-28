import math
import cmath
import string

# x = input("numberX")
# z = input("numberZ")
# y = input("numberY")
# if int(x) > int(y): print(int(x) - int(y))
#
# print(int(x) + int(y) + math.floor(float(z)))

# print(cmath.sqrt(-1))
# x = 'sdjsjgs'
# print(x[3])

# months = ['sd', 'sx', 'zx'] + 3 * ["cv"] + [1, 2, 3]
# print(months[8])
#
# x = max(1, 2, 3, 3, 3)
# print(x)

# x = (1, 2, 3, 9, 7, 4, 6, 5)  # 元组
# y = sorted(x)
# del y[1]
# y.remove(9)
# print(y)

# x = "{name}是个大帅比{value:.3f}".format(name=input("name:"), value=math.pi * int(input("value:")))
# print(x)


# x="the number is {num:.3f}".format(num=42)
# x = "the number is {num:b}".format(num=42)
# x = "the number is {num:c}".format(num=42)
# x = "the number is {num:d}".format(num=42)
# x = "the number is {num:e}".format(num=42)
# x = "the number is {num:o}".format(num=42)
# x = "the number is {num:s}".format(num='sds')
# x = "the number is {num:x}".format(num=42)
# x = "the number is {num:.2%}".format(num=0.42)
# x = "the number is {num:20}".format(num=45555)
# x = "the number is '{num:20.2}'".format(num="gdwugeugw")

# x = '{:015.3f}\n'.format(math.pi)  # 0来填充数字
# y = '{:<15.3f}\n'.format(math.pi)  # 左对齐
# z = '{:>15.3f}\n'.format(math.pi)  # 右对齐
# n = '{:@>15.3f}'.format(math.pi)  # 右对齐，指定符号填充
# print(x + y + z + n)

# print(string.digits)

x = {"name": "xqd",
     "age": "26",
     "sex": "man"}
# del x["hg"] #删除字典项 如果没有这个key的话会报错
# x.pop("name")  #也是删除字典项，如果没有这个key的话会报错
print(x.items())  # 转换为列表
print(x.keys())  # 获取所有键的列表
print(x.values())  # 获取所有值的列表
