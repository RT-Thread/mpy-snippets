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

PIN_OUT = 31   # PB15, get the pin number from get_pin_number.py
PIN_IN  = 58   # PD10

p_out = Pin(("PB15", PIN_OUT), Pin.OUT_PP)
p_out.value(1)                 # set io high
p_out.value(0)                 # set io low

p_in = Pin(("key_0", PIN_IN), Pin.IN, Pin.PULL_UP)
print(p_in.value() )           # get value, 0 or 1
