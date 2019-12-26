#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-12-10     SummerGift   first version
#

from camera import camera

cam = camera()
cam.snapshot("picture.jpg")