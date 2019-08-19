import utime as time
from micropython import const
import ustruct as struct

AHT10_ADDR               = const(0x38)
AHT10_CALIBRATION_CMD    = const(0xE1)         # calibration cmd for measuring
AHT10_NORMAL_CMD         = const(0xA8)         # normal cmd
AHT10_GET_DATA           = const(0xAC)         # get data cmd

class AHT10:
    """Class which provides interface to MPU6500 6-axis motion tracking device."""
    def __init__(self, i2c, address=0x38):
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