# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-28     SummerGift   first version
#

def get_pin_num(pin_index):
    """
    Get the GPIO pin number through the GPIO index, format must be "P + <A~K> + number", such as PE7
    """

    if pin_index[0] != 'P':
        print("ERROR : Please pass in the correct parameters P + <A~K> + number, such as PE7")
        return

    if not pin_index[1].isupper():
        print("ERROR : Please pass in the correct parameters P + <A~K> + number, such as PE7")
        return

    return (ord(pin_index[1]) - ord('A')) * 16 + int(pin_index[2:])

print("The pin number of PE7 is %d, then blink the red led."%get_pin_num("PE7")) # Get the pin number for PE7

# then you can use the pin num to control the device, such as led:

import utime as time
from machine import Pin

# create led object from get_pin_num("PE7") and set pin to output mode
led = Pin(("led_red", get_pin_num("PE7")), Pin.OUT_PP)

while True:
    led.value(0)  # Set led turn on
    time.sleep(0.5)
    led.value(1)  # Set led turn off
    time.sleep(0.5)
