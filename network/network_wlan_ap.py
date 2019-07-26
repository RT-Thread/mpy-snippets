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

ap = network.WLAN(network.AP_IF)
ap.config(essid="hello_rt-thread", password="88888888")
ap.active(True)
ap.config("essid")
