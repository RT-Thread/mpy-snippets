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

class AP3216C:
    """Class which provides interface to apc3216c device."""
    def __init__(self, i2c, address=AP3216C_ADDR):
        self.i2c = i2c
        self.address = address

    def sensor_init(self):
        buf=bytearray(2)
        buf[0] = 0x00
        buf[1] = 0x00
        self.i2c.writeto_mem(self.address, AHT10_NORMAL_CMD, buf)
        time.sleep_ms(350)
        buf[0] = 0x08
        buf[1] = 0x00
        self.i2c.writeto_mem(self.address, AHT10_CALIBRATION_CMD, buf)
        time.sleep_ms(450)

        # /* reset ap3216c
        # reset_sensor(dev)
        # rt_thread_delay(rt_tick_from_millisecond(100))# // delay at least  100ms

        # ap3216c_set_param(dev, AP3216C_SYSTEM_MODE, AP3216C_MODE_ALS_AND_PS);
        # rt_thread_delay(rt_tick_from_millisecond(100)); // delay at least  100ms

    def reset_sensor(self):

        buf=bytearray(2)
        buf[0] = 0x00
        buf[1] = 0x00
        self.i2c.writeto_mem(self.address, AHT10_NORMAL_CMD, buf)

        time.sleep_ms(100)

    def is_calibration_enabled(self):
        status = self.i2c.readfrom(self.address, 1)
        status_hex = struct.unpack_from(">b", status)
        if status_hex[0] & int('0x68', 16) == int('0x08', 16):
            return True
        else:
            return False

    def read_temperature(self):
        cmd=bytearray(2)
        cmd[0] = 0x00
        cmd[1] = 0x00
        self.i2c.writeto_mem(self.address, AHT10_GET_DATA, cmd)

        if self.is_calibration_enabled():
            temp = self.i2c.readfrom(self.address, 6)
            temp_hex = struct.unpack(">BBBBBB", temp)
            cur_temp = ((temp_hex[3] & 0xf) << 16 | temp_hex[4] << 8 | temp_hex[5]) * 200.0 / (1 << 20) - 50
            return cur_temp
        else:
            self.sensor_init()
            print("The aht10 is under an abnormal status. Please try again")

    def read_humidity(self):
        cmd=bytearray(2)
        cmd[0] = 0x00
        cmd[1] = 0x00
        self.i2c.writeto_mem(self.address, AHT10_GET_DATA, cmd)

        if self.is_calibration_enabled():
            temp = self.i2c.readfrom(self.address, 6)
            temp_hex = struct.unpack(">BBBBBB", temp)

            while temp_hex[2] == 0:
                temp = self.i2c.readfrom(self.address, 6)
                temp_hex = struct.unpack(">BBBBBB", temp)

            cur_humi = (temp_hex[1] << 12 | temp_hex[2] << 4 | (temp_hex[3] & 0xf0) >> 4) * 100.0 / (1 << 20)
            return cur_humi
        else:
            self.sensor_init()
            print("The aht10 is under an abnormal status. Please try again")