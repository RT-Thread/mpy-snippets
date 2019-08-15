# The MIT License (MIT)
#
# Copyright (c) 2017 Tony DiCola for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_fxos8700`
====================================================

CircuitPython module for the NXP FXOS8700 accelerometer and magnetometer.
Based on the driver from: https://github.com/adafruit/Adafruit_FXOS8700

See examples/simpletest.py for a demo of the usage.

* Author(s): Tony DiCola

Implementation Notes
--------------------

**Hardware:**

*  Adafruit `Precision NXP 9-DOF Breakout Board - FXOS8700 + FXAS21002
   <https://www.adafruit.com/product/3463>`_ (Product ID: 3463)

**Software and Dependencies:**

* Adafruit CircuitPython firmware (2.2.0+) for the ESP8622 and M0-based boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
"""
try:
    import ustruct as struct
except ImportError:
    import struct

from machine import Pin, I2C
from micropython import const

# Register addresses and other constants:
# pylint: disable=bad-whitespace
_FXOS8700_ADDRESS               = const(0x1F)   # 0011111
_FXOS8700_ID                    = const(0xC7)   # 1100 0111
_FXOS8700_REGISTER_STATUS       = const(0x00)
_FXOS8700_REGISTER_OUT_X_MSB    = const(0x01)
_FXOS8700_REGISTER_OUT_X_LSB    = const(0x02)
_FXOS8700_REGISTER_OUT_Y_MSB    = const(0x03)
_FXOS8700_REGISTER_OUT_Y_LSB    = const(0x04)
_FXOS8700_REGISTER_OUT_Z_MSB    = const(0x05)
_FXOS8700_REGISTER_OUT_Z_LSB    = const(0x06)
_FXOS8700_REGISTER_WHO_AM_I     = const(0x0D)   # 11000111   r
_FXOS8700_REGISTER_XYZ_DATA_CFG = const(0x0E)
_FXOS8700_REGISTER_CTRL_REG1    = const(0x2A)   # 00000000   r/w
_FXOS8700_REGISTER_CTRL_REG2    = const(0x2B)   # 00000000   r/w
_FXOS8700_REGISTER_CTRL_REG3    = const(0x2C)   # 00000000   r/w
_FXOS8700_REGISTER_CTRL_REG4    = const(0x2D)   # 00000000   r/w
_FXOS8700_REGISTER_CTRL_REG5    = const(0x2E)   # 00000000   r/w
_FXOS8700_REGISTER_MSTATUS      = const(0x32)
_FXOS8700_REGISTER_MOUT_X_MSB   = const(0x33)
_FXOS8700_REGISTER_MOUT_X_LSB   = const(0x34)
_FXOS8700_REGISTER_MOUT_Y_MSB   = const(0x35)
_FXOS8700_REGISTER_MOUT_Y_LSB   = const(0x36)
_FXOS8700_REGISTER_MOUT_Z_MSB   = const(0x37)
_FXOS8700_REGISTER_MOUT_Z_LSB   = const(0x38)
_FXOS8700_REGISTER_MCTRL_REG1   = const(0x5B)   # 00000000   r/w
_FXOS8700_REGISTER_MCTRL_REG2   = const(0x5C)   # 00000000   r/w
_FXOS8700_REGISTER_MCTRL_REG3   = const(0x5D)   # 00000000   r/w
_ACCEL_MG_LSB_2G                = 0.000244
_ACCEL_MG_LSB_4G                = 0.000488
_ACCEL_MG_LSB_8G                = 0.000976
_MAG_UT_LSB                     = 0.1
_SENSORS_GRAVITY_STANDARD       = 9.80665
# pylint: enable=bad-whitespace

# User-facing constants/module-level globals:
ACCEL_RANGE_2G = 0x00
ACCEL_RANGE_4G = 0x01
ACCEL_RANGE_8G = 0x02


def _twos_comp(val, bits):
    # Convert an unsigned integer in 2's compliment form of the specified bit
    # length to its signed integer value and return it.
    if val & (1 << (bits - 1)) != 0:
        return val - (1 << bits)
    return val


class FXOS8700:
    """Driver for the NXP FXOS8700 accelerometer and magnetometer."""
    # Class-level buffer for reading and writing data with the sensor.
    # This reduces memory allocations but means the code is not re-entrant or
    # thread safe!
    _BUFFER = bytearray(13)

    def __init__(self, i2c, address=_FXOS8700_ADDRESS,
                 accel_range=ACCEL_RANGE_2G):
        assert accel_range in (ACCEL_RANGE_2G, ACCEL_RANGE_4G, ACCEL_RANGE_8G)
        self._accel_range = accel_range
        self._device = i2c
        self.slave_addr = address

        # Check for chip ID value.
        if self._read_u8(_FXOS8700_REGISTER_WHO_AM_I) != _FXOS8700_ID:
            raise RuntimeError('Failed to find FXOS8700, check wiring!')
        # Set to standby mode (required to make changes to this register)
        self._write_u8(_FXOS8700_REGISTER_CTRL_REG1, 0)
        if accel_range == ACCEL_RANGE_2G:
            self._write_u8(_FXOS8700_REGISTER_XYZ_DATA_CFG, 0x00)
        elif accel_range == ACCEL_RANGE_4G:
            self._write_u8(_FXOS8700_REGISTER_XYZ_DATA_CFG, 0x01)
        elif accel_range == ACCEL_RANGE_8G:
            self._write_u8(_FXOS8700_REGISTER_XYZ_DATA_CFG, 0x02)
        # High resolution
        self._write_u8(_FXOS8700_REGISTER_CTRL_REG2, 0x02)
        # Active, Normal Mode, Low Noise, 100Hz in Hybrid Mode
        self._write_u8(_FXOS8700_REGISTER_CTRL_REG1, 0x15)
        # Configure the magnetometer
        # Hybrid Mode, Over Sampling Rate = 16
        self._write_u8(_FXOS8700_REGISTER_MCTRL_REG1, 0x1F)
        # Jump to reg 0x33 after reading 0x06
        self._write_u8(_FXOS8700_REGISTER_MCTRL_REG2, 0x20)

    def _read_u8(self, address):
        # Read an 8-bit unsigned value from the specified 8-bit address.
        self._BUFFER = bytearray(1)
        self._BUFFER[0] = address & 0xFF

        self._BUFFER = self._device.readfrom_mem(self.slave_addr, address, 1)
        return self._BUFFER[0]

    def _write_u8(self, address, val):
        # Write an 8-bit unsigned value to the specified 8-bit address.
        # with self._device as i2c:
        self._BUFFER = bytearray(2)
        self._BUFFER[0] = address & 0xFF
        self._BUFFER[1] = val & 0xFF
        self._device.writeto(self.slave_addr, self._BUFFER)

    def read_raw_accel_mag(self):
        """Read the raw accelerometer and magnetometer readings.  Returns a
        2-tuple of 3-tuples:

        - Accelerometer X, Y, Z axis 14-bit signed raw values
        - Magnetometer X, Y, Z axis 16-bit signed raw values

        If you want the acceleration or magnetometer values in friendly units
        consider using the accelerometer and magnetometer properties!
        """
        # Read accelerometer data from sensor.
        self._BUFFER = bytearray(6)
        self._BUFFER = self._device.readfrom_mem(self.slave_addr, _FXOS8700_REGISTER_OUT_X_MSB, 6)
        accel_raw_x = struct.unpack_from('>H', self._BUFFER[0:2])[0]
        accel_raw_y = struct.unpack_from('>H', self._BUFFER[2:4])[0]
        accel_raw_z = struct.unpack_from('>H', self._BUFFER[4:6])[0]
        # Convert accelerometer data to signed 14-bit value from 16-bit
        # left aligned 2's compliment value.
        accel_raw_x = _twos_comp(accel_raw_x >> 2, 14)
        accel_raw_y = _twos_comp(accel_raw_y >> 2, 14)
        accel_raw_z = _twos_comp(accel_raw_z >> 2, 14)
        # Read magnetometer data from sensor.  No need to convert as this is
        # 16-bit signed data so struct parsing can handle it directly.
        self._BUFFER = bytearray(6)
        self._BUFFER = self._device.readfrom_mem(self.slave_addr, _FXOS8700_REGISTER_MOUT_X_MSB, 6)
        mag_raw_x = struct.unpack_from('>h', self._BUFFER[0:2])[0]
        mag_raw_y = struct.unpack_from('>h', self._BUFFER[2:4])[0]
        mag_raw_z = struct.unpack_from('>h', self._BUFFER[4:6])[0]
        return ((accel_raw_x, accel_raw_y, accel_raw_z),
                (mag_raw_x, mag_raw_y, mag_raw_z))

    @property
    def accelerometer(self):
        """Read the acceleration from the accelerometer and return its X, Y, Z axis values as a
           3-tuple in m/s^2.
        """
        accel_raw, _ = self.read_raw_accel_mag()
        # Convert accel values to m/s^2
        factor = 0
        if self._accel_range == ACCEL_RANGE_2G:
            factor = _ACCEL_MG_LSB_2G
        elif self._accel_range == ACCEL_RANGE_4G:
            factor = _ACCEL_MG_LSB_4G
        elif self._accel_range == ACCEL_RANGE_8G:
            factor = _ACCEL_MG_LSB_8G
        return [x * factor * _SENSORS_GRAVITY_STANDARD for x in accel_raw]

    @property
    def magnetometer(self):
        """Read the magnetometer values and return its X, Y, Z axis values as a 3-tuple in uTeslas.
        """
        _, mag_raw = self.read_raw_accel_mag()
        # Convert mag values to uTesla
        return [x * _MAG_UT_LSB for x in mag_raw]
