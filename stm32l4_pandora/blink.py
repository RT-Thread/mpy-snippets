# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

import utime as time
from machine import Pin

PIN_LED_R = 71    # PE7, get the pin number from get_pin_number.py

# create led object from pin PIN_LED_R, Set pin PIN_LED_R to output mode
led = Pin(("led_red", PIN_LED_R), Pin.OUT_PP)

while True:
    led.value(0)  # Set led turn on
    time.sleep(0.5)
    led.value(1)  # Set led turn off
    time.sleep(0.5)
