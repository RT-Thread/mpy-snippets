from machine import I2C, Pin
from ap3216c import AP3216C

PIN_CLK = 32   # PC0, get the pin number from get_pin_number.py
PIN_SDA = 33   # PC1

clk = Pin(("clk", PIN_CLK), Pin.OUT_OD)   # Select the PIN_CLK as the clock
sda = Pin(("sda", PIN_SDA), Pin.OUT_OD)   # Select the PIN_SDA as the data line

i2c = I2C(-1, clk, sda, freq=100000)
print(i2c.scan())

sensor = AP3216C(i2c)
# sensor.sensor_init()
# sensor.is_calibration_enabled()

AP3216C_MODE_POWER_DOWN       = const(0x00)    # Power down (Default)
AP3216C_MODE_ALS              = const(0x01)    # ALS function active
AP3216C_MODE_PS               = const(0x02)    # PS+IR function active
AP3216C_MODE_ALS_AND_PS       = const(0x03)    # ALS and PS+IR functions active
AP3216C_MODE_SW_RESET         = const(0x04)    # SW reset
AP3216C_MODE_ALS_ONCE         = const(0x05)    # ALS function once
AP3216C_MODE_PS_ONCE          = const(0x06)    # PS+IR function once
AP3216C_MODE_ALS_AND_PS_ONCE  = const(0x07)    # ALS and PS+IR functions once

print(ap3216c_mode_enum_value.AP3216C_MODE_POWER_DOWN)
