# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-07-27     SummerGift   first version
#

# Python 中的循环语句有 for 和 while

# 下列程序使用 while 来计算 1 到 100 的总和：
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("The sum from 1 to %d is: %d" % (n, sum))

# Python for 循环可以遍历任何序列的项目，如一个列表或者一个字符串
languages = ["C", "C++", "java", "Python"] 
for x in languages:
    print (x)

# 如果你需要遍历数字序列，可以使用内置 range() 函数。它会生成数列，例如:
for i in range(5):
    print(i)

# Python pass 是空语句，是为了保持程序结构的完整性
# pass 不做任何事情，一般用做占位语句，如下实例

# while True:
#     pass  # 等待键盘中断 (Ctrl+C)

# 以下实例在字母为 r 时 执行 pass 语句块:
for letter in 'RT-Thread':
    if letter == 'T':
        pass
        print('exec pass code')
    else:
        print("current letter : %s" % letter)

print("exit!")
