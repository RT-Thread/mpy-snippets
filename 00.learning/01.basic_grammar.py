#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-07-27     SummerGift   first version
#

# 在 Python 中将需要注释的内容前加上 # 号
# 第一个注释
import sys
print("Hello, Python!")  # 第二个注释

# Python 最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
if True:
    print("True")
else:
    print("False")

# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *

import sys
print(sys.version)

from sys import path
print ('python path %s'%path)

# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

counter = 100          # 整型变量
miles = 1000.0       # 浮点型变量
name = "RT-Thread"     # 字符串

print(counter)
print(miles)
print(name)

# Python3 中有六个标准的数据类型：

# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
