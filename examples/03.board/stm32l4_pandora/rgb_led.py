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

LED_ON  = 0
LED_OFF = 1

led_r = Pin(("LED RED", pin_num("PE7")), Pin.OUT_PP)
led_g = Pin(("LED GREEN", pin_num("PE8")), Pin.OUT_PP)
led_b = Pin(("LED BLUE", pin_num("PE9")), Pin.OUT_PP)

blink_tab = [(LED_ON, LED_ON, LED_ON),
             (LED_OFF, LED_ON, LED_ON),
             (LED_ON, LED_OFF, LED_ON),
             (LED_ON, LED_ON, LED_OFF),
             (LED_OFF, LED_OFF, LED_ON),
             (LED_ON, LED_OFF, LED_OFF),
             (LED_OFF, LED_ON, LED_OFF),
             (LED_ON, LED_OFF, LED_OFF)]

count = 0

while True:
    group_num = count % len(blink_tab)

    led_r.value(blink_tab[group_num][0])           # set led status
    led_g.value(blink_tab[group_num][1])
    led_b.value(blink_tab[group_num][2])

    count += 1
    time.sleep(0.5)
