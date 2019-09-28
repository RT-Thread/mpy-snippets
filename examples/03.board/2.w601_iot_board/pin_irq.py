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

PIN_KEY0 = 35    # PA7

key_0 = Pin(("key_0", PIN_KEY0), Pin.IN, Pin.PULL_UP)

def func(v):
    print("Hello rt-thread!")

key_0.irq(trigger=Pin.IRQ_RISING, handler=func)
