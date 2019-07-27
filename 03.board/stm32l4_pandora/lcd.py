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
lcd.fill(lcd.BLACK)                     # Fill the entire LCD with black
lcd.fill(lcd.RED)                       # Fill the entire LCD with red
lcd.fill(lcd.GRAY)                      # Fill the entire LCD with gray
lcd.fill(lcd.WHITE)                     # Fill the entire LCD with white
lcd.pixel(50, 50, lcd.BLUE)             # fills the pixels in the (50,50) position with blue
lcd.text("hello RT-Thread", 0, 0, 16)   # prints the string at 16 font size at position (0, 0)
lcd.text("hello RT-Thread", 0, 16, 24)  # prints the string at 24 font size at position (0, 16)
lcd.text("hello RT-Thread", 0, 48, 32)  # prints the string at 32 font size at position (0, 48)
lcd.line(0, 50, 239, 50)                # Draw a line starting at (0,50) and ending at (239,50)
lcd.line(0, 50, 239, 50)                # Draw a line starting at (0,50) and ending at (239,50)
lcd.rectangle(100, 100, 200, 200)       # Draw a rectangle with the top left corner (100,100) and the bottom right corner (200,200)
lcd.circle(150, 150, 80)                # Draw a circle with a radius of 80 at the center (150,150)
