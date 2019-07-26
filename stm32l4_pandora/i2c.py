# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

from machine import Pin, I2C

PIN_CLK = 29   # PB13, get the pin number from get_pin_number.py
PIN_SDA = 30   # PB14

clk = Pin(("clk", PIN_CLK), Pin.OUT_OD)   # Select the PIN_CLK pin device as the clock
sda = Pin(("sda", PIN_SDA), Pin.OUT_OD)   # Select the PIN_SDA pin device as the data line
i2c = I2C(-1, clk, sda, freq=100000)      # create I2C peripheral at frequency of 100kHz
i2c.scan()                                # scan for slaves, returning a list of 7-bit addresses
i2c.writeto(0x51, b'123')                 # write 3 bytes to slave with 7-bit address 42
i2c.readfrom(0x51, 4)                     # read 4 bytes from slave with 7-bit address 42
i2c.readfrom_mem(0x51, 0x02, 1)           # read 1 bytes from memory of slave 0x51(7-bit)
i2c.writeto_mem(0x51, 2, b'\x10')         # write 1 byte to memory of slave 42

