from machine import I2C, Pin
from aht10 import AHT10

PIN_CLK = 54   # PD6, get the pin number from get_pin_number.py
PIN_SDA = 33   # PC1

clk = Pin(("clk", PIN_CLK), Pin.OUT_OD)   # Select the PIN_CLK as the clock
sda = Pin(("sda", PIN_SDA), Pin.OUT_OD)   # Select the PIN_SDA as the data line

i2c = I2C(-1, clk, sda, freq=100000)
sensor = AHT10(i2c)
sensor.sensor_init()
sensor.is_calibration_enabled()
print("current temp: %.2f"%sensor.read_temperature())
print("current humi: %.2f"%sensor.read_humidity())
