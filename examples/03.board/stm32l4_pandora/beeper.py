#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

import utime as time
from machine import Pin

# Get the GPIO pin number from GPIO index, for details see pin_num example.
def pin_num(pin_index):
    return (ord(pin_index[1]) - ord('A')) * 16 + int(pin_index[2:])

# create beeper object from pin PIN_BEEPER, Set pin PIN_BEEPER to output mode
beeper = Pin(("beep", pin_num("PB2")), Pin.OUT_PP)

beeper.value(1)            # trun the buzzer on
time.sleep(0.5)
beeper.value(0)            # trun the buzzer off
time.sleep(0.5)
beeper.value(1)
time.sleep(0.5)
beeper.value(0)
time.sleep(0.5)
