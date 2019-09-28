#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

from machine import Pin

# Get the GPIO pin number from GPIO index, for details see pin_num example.

def pin_num(pin_index):
    return (ord(pin_index[1]) - ord('A')) * 16 + int(pin_index[2:])

key_0 = Pin(("key_0", pin_num("PD10")), Pin.IN, Pin.PULL_UP)

def func(v):
    print("Hello rt-thread!")

key_0.irq(trigger=Pin.IRQ_RISING, handler=func)
