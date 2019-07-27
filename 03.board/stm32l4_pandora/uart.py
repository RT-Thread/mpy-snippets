# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

from machine import UART

uart = UART(1, 115200)                          # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1)  # init with given parameters
uart.read(10)                                   # read 10 characters, returns a bytes object
uart.read()                                     # read all available characters
uart.readline()                                 # read a line
uart.write('abc')                               # write the 3 characters
