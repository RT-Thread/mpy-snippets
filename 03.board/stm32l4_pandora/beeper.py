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

PIN_BEEPER = 18    # PB2, get the pin number from get_pin_number.py

# create beeper object from pin PIN_BEEPER, Set pin PIN_BEEPER to output mode
beeper = Pin(("beep", PIN_BEEPER), Pin.OUT_PP)

beeper.value(1)            # trun the buzzer on
time.sleep(0.5)
beeper.value(0)            # trun the buzzer off
time.sleep(0.5)
beeper.value(1)
time.sleep(0.5)
beeper.value(0)
time.sleep(0.5)
