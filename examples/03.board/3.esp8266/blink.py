#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-09-27     SummerGift   first version
#

import time
from machine import Pin
led = Pin(2, Pin.OUT)  # create LED object from pin2,Set Pin2 to output

while True:
    led.value(1)  # turn off
    time.sleep(0.5)
    led.value(0)  # turn on
    time.sleep(0.5)
