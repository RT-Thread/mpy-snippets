from ssd1306 import SSD1306_I2C
from machine import Pin, I2C
# w601 iot board test
PIN_CLK = 66   # PB10
PIN_SDA = 65   # PB11
clk = Pin(("clk", PIN_CLK), Pin.OUT_OD)   # Select the PIN_CLK pin device as the clock
sda = Pin(("sda", PIN_SDA), Pin.OUT_OD)   # Select the PIN_SDA pin device as the data line
i2c = I2C(-1, clk, sda, freq=100000)
oled = SSD1306_I2C(128, 64, i2c)  


oled.draw_line(0,0,128,64)
oled.draw_line(128,0,0,64)
oled.show_text(0,0, "RTT test!",12)
oled.show_text(0,10, "RTT TEST!")
oled.show_text(0,24, "RTT test!", 24)
oled.show_text(0,48, "MicroPython")
oled.show()





