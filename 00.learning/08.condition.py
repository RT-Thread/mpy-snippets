# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-07-27     SummerGift   first version
#

# if 语句
# Python中if语句的一般形式如下所示：

# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3

# 如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
# 如果 "condition_1" 为False，将判断 "condition_2"
# 如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
# 如果 "condition_2" 为False，将执行"statement_block_3"块语句
# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else

# 注意：
# 1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块
# 3、在Python中没有switch – case语句

count1 = 100
if count1:
    print ("1 - if get condition true")
    print (count1)

count2 = 0
if count2:
    print ("2 - if get condition true")
    print (count2)

print ("exit!")
