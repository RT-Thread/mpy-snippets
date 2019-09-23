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

# Get the GPIO pin number from GPIO index, for details see pin_num example.
def pin_num(pin_index):
    return (ord(pin_index[1]) - ord('A')) * 16 + int(pin_index[2:])

# create led object from pin PIN_LED_R, Set pin PIN_LED_R to output mode
led = Pin(("led_red", pin_num("PE7")), Pin.OUT_PP)

while True:
    led.value(0)  # Set led turn on
    time.sleep(0.5)
    led.value(1)  # Set led turn off
    time.sleep(0.5)