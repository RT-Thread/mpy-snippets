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

adc = ADC("adc", 5)         # Creates an ADC object that currently uses the 5 channel(PB23) of an ADC device name "adc"
value = (adc.read() - 8192.0) / 8192 * 2.25 / 1.2 + 1.584  # Gets the ADC object sampling value and change to voltage value
print("Voltage Value: %.3f" % value)                       # print voltage value
adc.deinit()                # Close ADC object
adc.init(5)                 # Open and reconfigure the ADC object
