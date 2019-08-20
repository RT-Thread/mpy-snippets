import utime as time
from micropython import const
import ustruct as struct

# System Register
AP3216C_SYS_CONFIGURATION_REG     =  const(0x00)
AP3216C_SYS_INT_STATUS_REG        =  const(0x01)
AP3216C_SYS_INT_CLEAR_MANNER_REG  =  const(0x02)
AP3216C_IR_DATA_L_REG             =  const(0x0A)
AP3216C_IR_DATA_H_REG             =  const(0x0B)
AP3216C_ALS_DATA_L_REG            =  const(0x0C)
AP3216C_ALS_DATA_H_REG            =  const(0x0D)
AP3216C_PS_DATA_L_REG             =  const(0x0E)
AP3216C_PS_DATA_H_REG             =  const(0x0F)

# ALS Register
AP3216C_ALS_CONFIGURATION_REG     =  const(0x10) # range 5:4,persist 3:0
AP3216C_ALS_CALIBRATION_REG       =  const(0x19)
AP3216C_ALS_THRESHOLD_LOW_L_REG   =  const(0x1A) # bit 7:0
AP3216C_ALS_THRESHOLD_LOW_H_REG   =  const(0x1B) # bit 15:8
AP3216C_ALS_THRESHOLD_HIGH_L_REG  =  const(0x1C) # bit 7:0
AP3216C_ALS_THRESHOLD_HIGH_H_REG  =  const(0x1D) # bit 15:8

# PS Register
AP3216C_PS_CONFIGURATION_REG      =  const(0x20)
AP3216C_PS_LED_DRIVER_REG         =  const(0x21)
AP3216C_PS_INT_FORM_REG           =  const(0x22)
AP3216C_PS_MEAN_TIME_REG          =  const(0x23)
AP3216C_PS_LED_WAITING_TIME_REG   =  const(0x24)
AP3216C_PS_CALIBRATION_L_REG      =  const(0x28)
AP3216C_PS_CALIBRATION_H_REG      =  const(0x29)
AP3216C_PS_THRESHOLD_LOW_L_REG    =  const(0x2A) # bit 1:0
AP3216C_PS_THRESHOLD_LOW_H_REG    =  const(0x2B) # bit 9:2
AP3216C_PS_THRESHOLD_HIGH_L_REG   =  const(0x2C) # bit 1:0
AP3216C_PS_THRESHOLD_HIGH_H_REG   =  const(0x2D) # bit 9:2

# AP3216C ADDR
AP3216C_ADDR                      =  const(0x1e) # 0x3c=0x1e<<1

# AP3216C_MODE SET
AP3216C_MODE_POWER_DOWN           =  const(0x00) # Power down (Default)
AP3216C_MODE_ALS                  =  const(0x01) # ALS function active
AP3216C_MODE_PS                   =  const(0x02) # PS+IR function active
AP3216C_MODE_ALS_AND_PS           =  const(0x03) # ALS and PS+IR functions active
AP3216C_MODE_SW_RESET             =  const(0x04) # SW reset
AP3216C_MODE_ALS_ONCE             =  const(0x05) # ALS function once
AP3216C_MODE_PS_ONCE              =  const(0x06) # PS+IR function once
AP3216C_MODE_ALS_AND_PS_ONCE      =  const(0x07) # ALS and PS+IR functions once

AP3216C_ALS_RANGE_20661           =  const(0x00)              # Resolution = 0.35 lux/count(default).
AP3216C_ALS_RANGE_5162            =  const(0x01)              # Resolution = 0.0788 lux/count.
AP3216C_ALS_RANGE_1291            =  const(0x02)              # Resolution = 0.0197 lux/count.
AP3216C_ALS_RANGE_323             =  const(0x03)              # Resolution = 0.0049 lux/count

class AP3216C:
    """Class which provides interface to apc3216c device."""
    def __init__(self, i2c, address=AP3216C_ADDR):
        self.i2c = i2c
        self.address = address

    def sensor_init(self):
        self.reset_sensor()

        buf=bytearray(1)
        buf[0]=AP3216C_MODE_ALS_AND_PS
        self.i2c.writeto_mem(self.address, AP3216C_SYS_CONFIGURATION_REG, buf)
        time.sleep_ms(100)

    def reset_sensor(self):
        buf=bytearray(1)
        buf[0]=AP3216C_MODE_SW_RESET
        self.i2c.writeto_mem(self.address, AP3216C_SYS_CONFIGURATION_REG, buf)
        time.sleep_ms(100)

    def read_ps_data(self):
        temp = self.i2c.readfrom_mem(self.address, AP3216C_PS_DATA_L_REG, 1)
        temp_hex1 = struct.unpack(">B", temp)
        temp = self.i2c.readfrom_mem(self.address, AP3216C_PS_DATA_H_REG, 1)
        temp_hex2 = struct.unpack(">B", temp)
        read_data = temp_hex1[0] + (temp_hex2[0] << 8)

        if (1 == ((read_data >> 6) & 0x01 or (read_data >> 14) & 0x01)):
            print("The data of PS is invalid for high intensive IR light")

        return (read_data & 0x000f) + (((read_data >> 8) & 0x3f) << 4)    # sensor proximity converse to reality

    def read_ambient_light(self):
        temp = self.i2c.readfrom_mem(self.address, AP3216C_ALS_DATA_L_REG, 1)
        temp_hex1 = struct.unpack(">B", temp)
        temp = self.i2c.readfrom_mem(self.address, AP3216C_ALS_DATA_H_REG, 1)
        temp_hex2 = struct.unpack(">B", temp)
        read_data = temp_hex1[0] + (temp_hex2[0] << 8)

        temp = self.get_als_range()

        if (temp == AP3216C_ALS_RANGE_20661):
            brightness = 0.35 * read_data;   # sensor ambient light converse to reality
        elif (temp == AP3216C_ALS_RANGE_5162):
            brightness = 0.0788 * read_data; # sensor ambient light converse to reality
        elif (temp == AP3216C_ALS_RANGE_1291):
            brightness = 0.0197 * read_data; # sensor ambient light converse to reality
        elif (temp == AP3216C_ALS_RANGE_323):
            brightness = 0.0049 * read_data; # sensor ambient light converse to reality
        else:
            print("Failed to get range of ap3216c")

        return brightness

    def get_als_range(self):

        temp = self.i2c.readfrom_mem(self.address, AP3216C_ALS_CONFIGURATION_REG, 1)
        temp_hex = struct.unpack(">B", temp)
        temp = (temp_hex[0] & 0xff) >> 4

        if (temp == AP3216C_ALS_RANGE_20661) or (temp == AP3216C_ALS_RANGE_5162) or (temp == AP3216C_ALS_RANGE_1291) or (temp == AP3216C_ALS_RANGE_323):
            return temp
        else:
            print("Getting als dynamic range is wrong, please refer als_range")
            return False


        