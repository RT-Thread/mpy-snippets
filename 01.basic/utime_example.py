# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

import utime

utime.sleep(1)                                     # sleep for 1 second
utime.sleep_ms(500)                                # sleep for 500 milliseconds
utime.sleep_us(10)                                 # sleep for 10 microseconds

start = utime.ticks_ms()                           # get value of millisecond counter
delta = utime.ticks_diff(utime.ticks_ms(), start)  # compute time difference
print(utime.ticks_add(utime.ticks_ms(), -100))
print(utime.ticks_add(0, -1))


