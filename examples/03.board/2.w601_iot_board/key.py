#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-08-26     SummerGift   first version
#

from machine import Pin

# You can get pin number information from file pin_map.py
PIN_LED_R   = 30  # PA13
PIN_KEY0    = 35  # PA7
KEY_PRESSED = 0

# create led object from pin PIN_LED_R, Set pin PIN_LED_R to output mode
led = Pin(("led_red", PIN_LED_R), Pin.OUT_PP)
key_0 = Pin(("key_0", PIN_KEY0), Pin.IN, Pin.PULL_UP)

while True:
    if key_0.value() == KEY_PRESSED:
        led.value(0)  # Set led turn on
    else:
        led.value(1)
