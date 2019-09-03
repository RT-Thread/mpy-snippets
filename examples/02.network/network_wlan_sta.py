#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

import network

wlan = network.WLAN(network.STA_IF)
print(wlan.scan())

wlan.connect("test", "123456789")

if wlan.isconnected():
    print("wifi connect successful")
else:
    print("wifi connect failed")
