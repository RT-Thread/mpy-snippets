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

# Get the GPIO pin number from GPIO index, for details see pin_num example.
def pin_num(pin_index):
    return (ord(pin_index[1]) - ord('A')) * 16 + int(pin_index[2:])

clk = Pin(("clk", pin_num("PB10")), Pin.OUT_PP)          # Select the PIN_CLK pin device as the clock
mosi = Pin(("mosi", pin_num("PB11")), Pin.OUT_PP)       # Select the PIN_MOSI pin device as the mosi
miso = Pin(("miso", pin_num("PB12")), Pin.IN)           # Select the PIN_MISO pin device as the miso

spi = SPI(-1, 500000, polarity=0, phase=0, bits=8, firstbit=0, sck=clk, mosi=mosi, miso=miso)
print(spi)
spi.write("hello rt-thread!")
spi.read(10)
