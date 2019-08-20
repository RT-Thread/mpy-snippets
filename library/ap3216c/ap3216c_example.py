from machine import I2C, Pin
from ap3216c import AP3216C
import utime as time

PIN_CLK = 32   # PC0, get the pin number from get_pin_number.py
PIN_SDA = 33   # PC1

clk = Pin(("clk", PIN_CLK), Pin.OUT_OD)   # Select the PIN_CLK as the clock
sda = Pin(("sda", PIN_SDA), Pin.OUT_OD)   # Select the PIN_SDA as the data line

i2c = I2C(-1, clk, sda, freq=100000)

sensor = AP3216C(i2c)
sensor.sensor_init()

while True:
    print("current ps data   : %.2f"%sensor.read_ps_data())
    print("current brightness: %.2f"%sensor.read_ambient_light())
    time.sleep_ms(1000)

