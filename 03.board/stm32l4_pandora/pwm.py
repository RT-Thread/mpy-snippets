# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

from machine import PWM     # Import PWM class from machine

pwm = PWM(3, 3, 1000, 100)  # Create PWM object. Currently, 3 channels of PWM device numbered 3 are used. 
                            # The initialization frequency is 1000Hz and the duty ratio value is 100 (duty ratio is 100/255 = 39.22%).
pwm.freq(2000)              # Set the frequency of PWM object
pwm.freq()                  # Get the frequency of PWM object
print(pwm)                  # Show PWM object information
pwm.duty(200)               # Sets the duty ratio value of PWM object
pwm.duty()                  # Get the duty ratio value of PWM object
print(pwm)                  # Show PWM object information
pwm.deinit()                # Close PWM object
pwm.init(3, 1000, 100)      # Open and reconfigure the PWM object
print(pwm)                  # Show PWM object information
