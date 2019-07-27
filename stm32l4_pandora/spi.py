# 
# Copyright (c) 2006-2019, RT-Thread Development Team
# 
# SPDX-License-Identifier: MIT License
# 
# Change Logs:
# Date           Author       Notes
# 2019-06-13     SummerGift   first version
#

from machine import Pin, SPI

PIN_CLK  = 26   # PB10, get the pin number from get_pin_number.py
PIN_MOSI = 27   # PB11
PIN_MISO = 28   # PB12

clk = Pin(("clk", PIN_CLK), Pin.OUT_PP)          # Select the PIN_CLK pin device as the clock
mosi = Pin(("mosi", PIN_MOSI), Pin.OUT_PP)       # Select the PIN_MOSI pin device as the mosi
miso = Pin(("miso", PIN_MISO), Pin.IN)           # Select the PIN_MISO pin device as the miso

spi = SPI(-1, 500000, polarity = 0, phase = 0, bits = 8, firstbit = 0, sck = clk, mosi = mosi, miso = miso)
print(spi)
spi.write("hello rt-thread!")
spi.read(10)

