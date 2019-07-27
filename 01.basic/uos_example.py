# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

import uos

print("Get the current directory:")
print(uos.getcwd())

print("Create folder: rtthread")
uos.mkdir("rtthread")

print("List the files in the current directory:")
print(uos.listdir())

print("Move the current directory to the rtthread folder:")
uos.chdir("rtthread")

print("Get the current directory:")
print(uos.getcwd())

print("Switch to the previous directory:")
uos.chdir("..")

print("Get the current directory:")
print(uos.getcwd())

print("List the files in the current directory:")
print(uos.listdir())

print("Delete the rtthread folder:")
uos.rmdir("rtthread")

print("List the files in the current directory:")
print(uos.listdir())
