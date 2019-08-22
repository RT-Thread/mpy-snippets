from machine import I2C, Pin
from icm20608 import ICM20608
import utime as time

PIN_CLK = 32   # PC0, get the pin number from get_pin_number.py
PIN_SDA = 33   # PC1

clk = Pin(("clk", PIN_CLK), Pin.OUT_OD)   # Select the PIN_CLK as the clock
sda = Pin(("sda", PIN_SDA), Pin.OUT_OD)   # Select the PIN_SDA as the data line

i2c = I2C(-1, clk, sda, freq=100000)
sensor = ICM20608(i2c)
sensor.sensor_init()
sensor.calib_level(10)

count = 100
while count > 0:
    print("accel : [ x : %10.2f y : %10.2f z : %10.2f]  gyro  : [ x : %10.2f y : %10.2f z : %10.2f]"%(sensor.get_accel()[0],sensor.get_accel()[1],sensor.get_accel()[2],sensor.get_gyro()[0],sensor.get_gyro()[1],sensor.get_gyro()[2]))
    count -= 1
    time.sleep_ms(100)
