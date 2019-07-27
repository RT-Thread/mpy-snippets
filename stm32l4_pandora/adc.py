# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

from machine import ADC     # Import the ADC class from machine

adc = ADC(1, 13)            # Creates an ADC object that currently uses the 13 channels of an ADC device numbered 1
print(adc.read())           # Gets the ADC object sampling value, value range 0 to 4096
adc.deinit()                # Close ADC object
adc.init(13)                # Open and reconfigure the ADC object
