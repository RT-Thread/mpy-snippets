#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-11-29     SummerGift   first version
#

from camera import camera
import rtthread

rtthread.wifi_join("w0", "test", "123456789")
time.sleep(3)

cam = camera()
cam.server_start(5009)
# cam.snapshot("picture2.jpg")
# cam.server_stop()