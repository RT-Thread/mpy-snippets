#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-07-27     SummerGift   first version
#

# List（列表）
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 列表截取的语法格式如下：
# 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。

list = ['abcd', 786, 2.23, 'hello', 70.2]
tinylist = [123, 'hello']

print(list)             # 输出完整列表
print(list[0])          # 输出列表第一个元素
print(list[1:3])        # 从第二个开始输出到第三个元素
print(list[2:])         # 输出从第三个元素开始的所有元素
print(tinylist * 2)     # 输出两次列表
print(list + tinylist)  # 连接列表
