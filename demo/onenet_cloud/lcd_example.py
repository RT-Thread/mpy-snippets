#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

from machine import LCD     # Import the LCD class from machine

lcd = LCD()                             # Create a LCD object
lcd.light(False)                        # Close the backlight
lcd.light(True)                         # Open the backlight
lcd.set_color(lcd.WHITE, lcd.BLACK)     # Set background color and foreground color
lcd.fill(lcd.WHITE)                     # Fill the entire LCD with white

lcd.text("Onenet Cloud", 26, 48, 32)  # prints the string at 32 font size at position (0, 48)
lcd.text("demo", 90, 120, 32)  # prints the string at 32 font size at position (0, 48)
