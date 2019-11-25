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

LED_ON  = 0
LED_OFF = 1

# You can get pin number information from file pin_map.py
PIN_LED_R = 30  # PA13
PIN_LED_G = 31  # PA14
PIN_LED_B = 32  # PA15

led_r = Pin(("led_red", PIN_LED_R), Pin.OUT_PP)
led_g = Pin(("led_green", PIN_LED_G), Pin.OUT_PP)
led_b = Pin(("led_blue", PIN_LED_B), Pin.OUT_PP)

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
