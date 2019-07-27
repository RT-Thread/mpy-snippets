# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

from machine import RTC

rtc = RTC()                            # Create an RTC device object
rtc.init((2019,6,5,2,10,22,30,0))      # Set initialization time
print(rtc.now())                       # Get the current time
rtc.deinit()                           # Reset time to January 1, 2015
print(rtc.now())                       # Get the current time
