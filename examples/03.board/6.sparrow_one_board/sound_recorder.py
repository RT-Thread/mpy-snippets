#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-12-10     SummerGift   first version
#

from recorder import recorder
from player import player
import utime as time

record = recorder()
record.start("hello.wav")
time.sleep(5)
record.stop()

play = player()
play.set_volume(80)
play.opensong("hello.wav")
play.play()
time.sleep(5)
play.stop()