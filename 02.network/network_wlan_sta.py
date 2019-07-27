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
wlan.scan()
wlan.connect("rtthread", "02188888888")
wlan.isconnected()
