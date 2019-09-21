#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-06-28     SummerGift   first version
#

def pin_num(pin_index):
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

print("The pin number of PE7 is %d, then blink the red led."%pin_num("PE7")) # Get the pin number for PE7
