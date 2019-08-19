import utime
from machine import I2C, Pin
from mpu9250 import MPU9250

PIN_CLK = 29   # PB13, get the pin number from get_pin_number.py
PIN_SDA = 30   # PB14

clk = Pin(("clk", PIN_CLK), Pin.OUT_OD)   # Select the PIN_CLK as the clock
sda = Pin(("sda", PIN_SDA), Pin.OUT_OD)   # Select the PIN_SDA as the data line

i2c = I2C(-1, clk, sda, freq=100000)
sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    # print(sensor.magnetic)     # not support yet
    utime.sleep_ms(1000)
