import utime as time
from micropython import const
import ustruct as struct

# Register map for icm20608
ICM20608_CONFIG_REG            = const(0x1A)  # configuration:fifo, ext sync and dlpf
ICM20608_GYRO_CONFIG_REG       = const(0x1B)  # gyroscope configuration
ICM20608_ACCEL_CONFIG1_REG     = const(0x1C)  # accelerometer configuration
ICM20608_ACCEL_CONFIG2_REG     = const(0x1D)  # accelerometer configuration
ICM20608_INT_ENABLE_REG        = const(0x38)  # interrupt enable
ICM20608_ACCEL_MEAS            = const(0x3B)  # accelerometer measurements
ICM20608_GYRO_MEAS             = const(0x43)  # gyroscope measurements
ICM20608_PWR_MGMT1_REG         = const(0x6B)  # power management 1
ICM20608_PWR_MGMT2_REG         = const(0x6C)  # power management 2

ICM20608_ADDR                  = const(0x68)  # slave address, ad0 set 0

ICM20608_PWR_MGMT1             = const(0x00)  # power management 1
ICM20608_PWR_MGMT2             = const(0x01)  # power management 2
ICM20608_GYRO_CONFIG           = const(0x02)  # gyroscope configuration(range)
ICM20608_ACCEL_CONFIG1         = const(0x03)  # accelerometer configuration(range)
ICM20608_ACCEL_CONFIG2         = const(0x04)  # accelerometer configuration2
ICM20608_INT_ENABLE            = const(0x05)  # interrupt enable

ICM20608_GYROSCOPE_RANGE0      = const(0x00)  # ±250dps
ICM20608_GYROSCOPE_RANGE1      = const(0x01)  # ±500dps
ICM20608_GYROSCOPE_RANGE2      = const(0x02)  # ±1000dps
ICM20608_GYROSCOPE_RANGE3      = const(0x03)  # ±2000dps

ICM20608_ACCELEROMETER_RANGE0  = const(0x00)  # ±2g
ICM20608_ACCELEROMETER_RANGE1  = const(0x01)  # ±4g
ICM20608_ACCELEROMETER_RANGE2  = const(0x02)  # ±8g
ICM20608_ACCELEROMETER_RANGE3  = const(0x03)  # ±16g

class ICM20608:
    """Class which provides interface to MPU6500 6-axis motion tracking device."""
    def __init__(self, i2c, address=ICM20608_ADDR):
        self.i2c = i2c
        self.address = address
        self.calib_accel = None
        self.calib_gyro = None

    def sensor_init(self):

        # open 3 accelerometers and 3 gyroscope
        self._register_char(ICM20608_PWR_MGMT2, 0x00)

        # /* set gyroscope range, default 250 dps */
        self._register_char(ICM20608_GYRO_CONFIG, 0x00)

        # /* set accelerometer range, default 2g */
        self._register_char(ICM20608_ACCEL_CONFIG1, 0x00)

        # /* ACCEL_FCHOICE_B = 0 and A_DLPF_CFG[2:0] = 1 */
        self._register_char(ICM20608_ACCEL_CONFIG1, 0x01)

    def calib_level(self, times):
        accel = [0, 0, 0]
        gypo = [0, 0, 0]
        accel_offset = [0, 0, 0]
        gypo_offset = [0, 0, 0]

        for num in range(0, times):
            buf = self.get_accel()
            accel[0] += buf[0]
            accel[1] += buf[1]
            accel[2] += buf[2]

            buf = self.get_gyro()
            gypo[0] += buf[0]
            gypo[1] += buf[1]
            gypo[2] += buf[2]

        accel_offset[0] = accel[0] / times
        accel_offset[1] = accel[1] / times
        accel_offset[2] = accel[2] / times

        gypo_offset[0] = gypo[0] / times
        gypo_offset[1] = gypo[1] / times
        gypo_offset[2] = gypo[2] / times

        self.calib_accel = accel_offset
        self.calib_gyro = gypo_offset

        return (accel_offset, gypo_offset)

    def get_accel(self):

        if self.get_accel_range() < 4:
            xyz = self._register_six_char(ICM20608_ACCEL_MEAS)
            buf=bytearray(2)
            buf[0] = xyz[1]
            buf[1] = xyz[0]
            accel_x = struct.unpack("<h", buf)

            buf=bytearray(2)
            buf[0] = xyz[3]
            buf[1] = xyz[2]
            accel_y = struct.unpack("<h", buf)

            buf=bytearray(2)
            buf[0] = xyz[5]
            buf[1] = xyz[4]
            accel_z = struct.unpack("<h", buf)

            if self.calib_accel == None:
                return [accel_x[0], accel_y[0], accel_z[0]]
            else:
                return [accel_x[0] - self.calib_accel[0], accel_y[0] - self.calib_accel[1], accel_z[0] - self.calib_accel[2]]

    def get_gyro(self):
        if self.get_accel_range() < 4:
            xyz = self._register_six_char(ICM20608_GYRO_MEAS)
            buf=bytearray(2)
            buf[0] = xyz[1]
            buf[1] = xyz[0]
            gyro_x = struct.unpack("<h", buf)

            buf=bytearray(2)
            buf[0] = xyz[3]
            buf[1] = xyz[2]
            gyro_y = struct.unpack("<h", buf)

            buf=bytearray(2)
            buf[0] = xyz[5]
            buf[1] = xyz[4]
            gyro_z = struct.unpack("<h", buf)
            
            if self.calib_gyro == None:
                return [gyro_x[0], gyro_y[0], gyro_z[0]]
            else:
                return [gyro_x[0] - self.calib_gyro[0], gyro_x[0] - self.calib_gyro[1], gyro_x[0] - self.calib_gyro[2]]

    def get_accel_range(self):
        range = self._register_char(ICM20608_ACCEL_CONFIG1_REG)  # default 2g
        return (range >> 3) & 0x3

    def get_gyro_range(self):
        range = self._register_char(ICM20608_GYRO_CONFIG_REG)  # default ±250dps
        return (range >> 3) & 0x3

    def _register_char(self, register, value=None, buf=bytearray(1)):
        if value is None:
            self.i2c.readfrom_mem_into(self.address, register, buf)
            return buf[0]

        struct.pack_into("<b", buf, 0, value)
        return self.i2c.writeto_mem(self.address, register, buf)

    def _register_three_shorts(self, register, buf=bytearray(6)):
        self.i2c.readfrom_mem_into(self.address, register, buf)
        return struct.unpack("<hhh", buf)

    def _register_six_char(self, register, buf=bytearray(6)):
        self.i2c.readfrom_mem_into(self.address, register, buf)
        return struct.unpack("<BBBBBB", buf)
