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

p_out = Pin(("PIN_OUT", pin_num("PB15")), Pin.OUT_PP)
p_out.value(1)                 # set io high
p_out.value(0)                 # set io low

p_in = Pin(("key_0", pin_num("PD10")), Pin.IN, Pin.PULL_UP)
print(p_in.value() )           # get value, 0 or 1
