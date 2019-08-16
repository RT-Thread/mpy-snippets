from machine import I2C, Pin
from get_pin_num import get_pin_num
from aht10 import AHT10

PIN_CLK = 29   # PB13, get the pin number from get_pin_number.py
PIN_SDA = 30   # PB14

clk = Pin(("clk", get_pin_num("PD6")), Pin.OUT_OD)   # Select the PIN_CLK as the clock
sda = Pin(("sda", get_pin_num("PC1")), Pin.OUT_OD)   # Select the PIN_SDA as the data line

i2c = I2C(-1, clk, sda, freq=100000)
sensor = AHT10(i2c)
sensor.sensor_init()
sensor.is_calibration_enabled()
print(sensor.read_temperature())
print(sensor.read_humidity())