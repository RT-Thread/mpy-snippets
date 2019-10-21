#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-09-27     SummerGift   first version
#

# pyboard V1.1
from pyb import LED
import time
led1 = LED(1)
led1.toggle()  # turn on led
led2 = LED(2)
led2.toggle()
led3 = LED(3)
led3.toggle()
led4 = LED(4)
led4.toggle()

while 1:
    time.sleep(0.5)
    led1.on()
    time.sleep(0.5)
    led1.off()
    time.sleep(0.5)
    led3.on()
    time.sleep(0.5)
    led3.off()
    time.sleep(0.5)
    led2.on()
    time.sleep(0.5)
    led2.off()
    time.sleep(0.5)
    led4.on()
    time.sleep(0.5)
    led4.off()
