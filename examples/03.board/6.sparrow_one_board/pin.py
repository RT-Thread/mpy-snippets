#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-11-29     SummerGift   first version
#

from machine import Pin

p_in = Pin(("key", 13), Pin.IN, Pin.PULL_UP)
print(p_in.value())   # get value, flase or true
