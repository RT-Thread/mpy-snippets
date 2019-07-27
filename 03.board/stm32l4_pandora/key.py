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

PIN_LED_R   = 71    # PE7, get the pin number from get_pin_number.py
PIN_KEY0    = 58    # PD10
KEY_PRESSED = 0

# create led object from pin PIN_LED_R, Set pin PIN_LED_R to output mode
led = Pin(("led_red", PIN_LED_R), Pin.OUT_PP)
key_0 = Pin(("key_0", PIN_KEY0), Pin.IN, Pin.PULL_UP)

while True:
    if key_0.value() == KEY_PRESSED:
        led.value(0)  # Set led turn on
    else:
        led.value(1)
