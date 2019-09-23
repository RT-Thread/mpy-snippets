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

# create led object from pin PIN_LED_R, Set pin PIN_LED_R to output mode
led = Pin(("led_red", pin_num("PE7")), Pin.OUT_PP)
key_0 = Pin(("key_0", pin_num("PD10")), Pin.IN, Pin.PULL_UP)

while True:
    if key_0.value() == 0:
        led.value(0)  # Set led turn on
    else:
        led.value(1)
