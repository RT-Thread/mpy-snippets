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

def func(v):
    print("Hello rt-thread!")

# Get the GPIO pin number from GPIO index, for details see pin_num example.
key_0 = Pin(("key_0", 13), Pin.IN, Pin.PULL_UP)
key_0.irq(trigger=Pin.IRQ_RISING, handler=func)
key_0 = Pin(("key_0", 13), Pin.IN, Pin.PULL_UP)
