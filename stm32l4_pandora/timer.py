# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-29     ChenYong     first version
#

def callback_periodic(obj):                                # defined  preiodic mode timeout callback
    print("Timer callback periodic test")

def callback_oneshot(obj):                                 # defined  ont shot mode timeout callback
    print("Timer callback oneshot test")

from machine import Timer
import utime as time

timer = Timer(15)                                          # Create Timer object. Timer device number 15 are used. 
timer.init(timer.PERIODIC, 1000, callback_periodic)        # Initialize the Timer device object
                                                           # Set Timer mode to preiodic mode, set timeout to 1 seconds and set callback fucntion
time.sleep_ms(5500)                                        # Execute 5 times timeout callback in the delay time
timer.init(timer.ONE_SHOT, 1000, callback_oneshot)         # Reset initialize the Timer device object
                                                           # Set Timer mode to one shot mode, set timeout to 1 seconds and set callback fucntion
time.sleep_ms(1500)                                        # Execute 1 times timeout callback in the delay time
timer.deinit()                                             # Stop and close Timer device object
