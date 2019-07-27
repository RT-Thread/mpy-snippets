# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-29     ChenYong     first version
#

from machine import WDT

wdt = WDT(10)                # Create an WDT device object, set the timeout to 10 seconds
wdt.feed()                   # Perform the "feed dog" operation to clear the watchdog device count during the timout period
                             # If not executed, the system will restart after the timeout
print("reset system after 10 seconds")
