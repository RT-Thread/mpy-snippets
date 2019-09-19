"""The ``machine`` module contains specific functions related to the hardware
on a particular board. Most functions in this module allow to achieve
direct and unrestricted access to and control of hardware blocks on a
system (like CPU, timers, buses, etc.). Used incorrectly, this can
lead to malfunction, lockups, crashes of your board, and in extreme
cases, hardware damage.

A note of callbacks used by functions and class methods of machine
module: all these callbacks should be considered as executing in an
interrupt context. This is true for both physical devices with
IDs >= 0 and “virtual” devices with negative IDs like -1 (these
“virtual” devices are still thin shims on top of real hardware
and real hardware interrupts).
"""


from typing import Callable, Optional, Collection, Union, Any


IDLE = ...  # type: int
SLEEP = ...  # type: int
DEEPSLEEP = ...  # type: int

PWRON_RESET = ...  # type: int
HARD_RESET = ...  # type: int
WDT_RESET = ...  # type: int
DEEPSLEEP_RESET = ...  # type: int
PIN_WAKE = ...  # type: int
RTC_WAKE = ... # type: int


class Pin(object):
    """A pin object is used to control I/O pins (also known as GPIO - general-purpose
input/output).  Pin objects are commonly associated with a physical pin that can
drive an output voltage and read input voltages.  The pin class has methods to set the mode of
the pin (IN, OUT, etc) and methods to get and set the digital logic level.
For analog control of a pin, see the :class:`ADC` class.

A pin object is constructed by using an identifier which unambiguously
specifies a certain I/O pin.  The allowed forms of the identifier and the
physical pin that the identifier maps to are port-specific.  Possibilities
for the identifier are an integer, a string or a tuple with port and pin
number.

Usage Model::

    from machine import Pin

    # create an output pin on pin #0
    p0 = Pin(0, Pin.OUT)

    # set the value low then high
    p0.value(0)
    p0.value(1)

    # create an input pin on pin #2, with a pull up resistor
    p2 = Pin(2, Pin.IN, Pin.PULL_UP)

    # read and print the pin value
    print(p2.value())

    # reconfigure pin #0 in input mode
    p0.mode(p0.IN)

    # configure an irq callback
    p0.irq(lambda p:print(p))
    """

    IRQ_FALLING = ...  # type: int
    IRQ_RISING = ...  # type: int
    IRQ_LOWLEVEL = ...  # type: int
    IRQ_HIGHLEVEL = ...  # type: int
    IN = ...  # type: int
    OUT = ...  # type: int
    OPEN_DRAIN = ...  # type: int
    PULL_UP = ...  # type: int
    PULL_DOWN = ...  # type: int
    LOW_POWER = ...  # type: int
    MED_POWER = ...  # type: int
    HIGH_POWER = ...  # type: int
    OUT_PP = ...  # type: int
    OUT_OD = ...  # type: int

    def __init__(self, id: Any, mode: int = -1, pull: int = -1, *,
                 value: Optional[int] = None,
                 drive: Optional[int] = None,
                 alt: Optional[int] = None) -> None:
        """Access the pin peripheral (GPIO pin) associated with the given ``id``.  If
   additional arguments are given in the constructor then they are used to initialise
   the pin.  Any settings that are not specified will remain in their previous state.

   The arguments are:

     - ``id`` is mandatory and can be an arbitrary object.  Among possible value
       types are: int (an internal Pin identifier), str (a Pin name), and tuple
       (pair of [port, pin]).

     - ``mode`` specifies the pin mode, which can be one of:

       - ``Pin.IN`` - Pin is configured for input.  If viewed as an output the pin
         is in high-impedance state.

       - ``Pin.OUT`` - Pin is configured for (normal) output.

       - ``Pin.OPEN_DRAIN`` - Pin is configured for open-drain output. Open-drain
         output works in the following way: if the output value is set to 0 the pin
         is active at a low level; if the output value is 1 the pin is in a high-impedance
         state.  Not all ports implement this mode, or some might only on certain pins.

       - ``Pin.ALT`` - Pin is configured to perform an alternative function, which is
         port specific.  For a pin configured in such a way any other Pin methods
         (except :meth:`Pin.init`) are not applicable (calling them will lead to undefined,
         or a hardware-specific, result).  Not all ports implement this mode.

       - ``Pin.ALT_OPEN_DRAIN`` - The Same as ``Pin.ALT``, but the pin is configured as
         open-drain.  Not all ports implement this mode.

     - ``pull`` specifies if the pin has a (weak) pull resistor attached, and can be
       one of:

       - ``None`` - No pull up or down resistor.
       - ``Pin.PULL_UP`` - Pull up resistor enabled.
       - ``Pin.PULL_DOWN`` - Pull down resistor enabled.

     - ``value`` is valid only for Pin.OUT and Pin.OPEN_DRAIN modes and specifies initial
       output pin value if given, otherwise the state of the pin peripheral remains
       unchanged.

     - ``drive`` specifies the output power of the pin and can be one of: ``Pin.LOW_POWER``,
       ``Pin.MED_POWER`` or ``Pin.HIGH_POWER``.  The actual current driving capabilities
       are port dependent.  Not all ports implement this argument.

     - ``alt`` specifies an alternate function for the pin and the values it can take are
       port dependent.  This argument is valid only for ``Pin.ALT`` and ``Pin.ALT_OPEN_DRAIN``
       modes.  It may be used when a pin supports more than one alternate function.  If only
       one pin alternate function is supported the this argument is not required.  Not all
       ports implement this argument.

   As specified above, the Pin class allows to set an alternate function for a particular
   pin, but it does not specify any further operations on such a pin.  Pins configured in
   alternate-function mode are usually not used as GPIO but are instead driven by other
   hardware peripherals.  The only operation supported on such a pin is re-initialising,
   by calling the constructor or :meth:`Pin.init` method.  If a pin that is configured in
   alternate-function mode is re-initialised with ``Pin.IN``, ``Pin.OUT``, or
   ``Pin.OPEN_DRAIN``, the alternate function will be removed from the pin.        """
        ...

    def init(self, value: int, drive: int, alt: int, mode: int = -1, pull: int = -1) -> None:
        """Re-initialise the pin using the given parameters. Only those arguments
        that are specified will be set. The rest of the pin peripheral state
        will remain unchanged. See the constructor documentation for details
        of the arguments.

        :param value: Initial output pin value.
        :param drive: Output power of the pin.
        :param alt: Alternate function for the pin.
        :param mode: Pin mode.
        :param pull: Flag that specifies if the pin has a (weak) pull resistor attached.
        """
        ...

    def value(self, x: Optional[int] = None) -> Optional[int]:
        """This method allows to set and get the value of the pin, depending on
        whether the argument **x** is supplied or not.

        If the argument is omitted then this method gets the digital logic
        level of the pin, returning 0 or 1 corresponding to low and high
        voltage signals respectively. The behaviour of this method depends
        on the mode of the pin:

        * ``Pin.IN`` - The method returns the actual input value currently present on the pin.
        * ``Pin.OUT`` - The behaviour and return value of the method is undefined.
        * ``Pin.OPEN_DRAIN`` - If the pin is in state ‘0’ then the behaviour and return value of the method is undefined. Otherwise, if the pin is in state ‘1’, the method returns the actual input value currently present on the pin.

        :param x: Value to set on a pin.
        :return: Current value of a pin.
        """
        ...

    def __call__(self, x: Optional[int]) -> Optional[int]:
        """Pin objects are callable. The call method provides a (fast) shortcut
        to set and get the value of the pin. It is equivalent to
        Pin.value([x]). See ``Pin.value()`` for more details.

        :param x: Value to set on a pin.
        :return: Current value of a pin.
        """
        ...

    def on(self) -> None:
        """Set pin to “1” output level."""
        ...

    def off(self) -> None:
        """Set pin to “0” output level."""
        ...

    def mode(self, mode: Optional[int]) -> Optional[int]:
        """Get or set the pin mode.

        **mode** can be one of following values:

        * ``Pin.IN`` - Pin is configured for input. If viewed as an output the pin is in high-impedance state.

        * ``Pin.OUT`` - Pin is configured for (normal) output.

        * ``Pin.OPEN_DRAIN`` - Pin is configured for open-drain output. Open-drain output works in the following way: if the output value is set to 0 the pin is active at a low level; if the output value is 1 the pin is in a high-impedance state. Not all ports implement this mode, or some might only on certain pins.

        * ``Pin.ALT`` - Pin is configured to perform an alternative function, which is port specific. For a pin configured in such a way any other Pin methods (except Pin.init()) are not applicable (calling them will lead to undefined, or a hardware-specific, result). Not all ports implement this mode.

        * ``Pin.ALT_OPEN_DRAIN`` - The Same as Pin.ALT, but the pin is configured as open-drain. Not all ports implement this mode.

        :param mode: Mode to be set on a pin.
        :return: Current mode on a pin.
        """
        ...

    def pull(self, pull: Optional[int]) -> Optional[int]:
        """Get or set the pin pull state.

        *pull* can be one of following values:

        * ``None`` - No pull up or down resistor.
        * ``Pin.PULL_UP`` - Pull up resistor enabled.
        * ``Pin.PULL_DOWN`` - Pull down resistor enabled.

        :param pull: Pull state.
        :return: Current pull state.
        """
        ...

    def irq(self, handler: Callable[[Pin], Any] = None, trigger: int = (IRQ_FALLING | IRQ_RISING),
            priority: int = 1, wake: int = None) -> Callable[[Pin], Any]:
        """
        Configure an interrupt handler to be called when the trigger source
        of the pin is active.

        If the pin mode is ``Pin.IN`` then the trigger
        source is the external value on the pin.

        If the pin mode is ``Pin.OUT`` then the trigger source is the output
        buffer of the pin.

        if the pin mode is ``Pin.OPEN_DRAIN`` then the trigger source is the
        output buffer for state ‘0’ and the external pin value for state ‘1’.

        Possible values for ``wake``:

        * ``machine.IDLE``
        * ``machine.SLEEP``
        * ``machine.DEEPSLEEP``

        Possible values for ``trigger``:

        * ``Pin.IRQ_FALLING`` - interrupt on falling edge.
        * ``Pin.IRQ_RISING`` - interrupt on rising edge.
        * ``Pin.IRQ_LOW_LEVEL`` - interrupt on low level.
        * ``Pin.IRQ_HIGH_LEVEL`` - interrupt on high level.

        These values can be OR’ed together to trigger on multiple events.

        :param handler: Interrupt handler.
        :param trigger: Event which can generate an interrupt
        :param priority: Priority level of the interrupt
        :param wake: Power mode in which this interrupt can wake up the system
        :return: Callback object.
        """
        ...


# class Signal(object):
#     def __init__(self, pin_obj: Pin, invert: bool = False) -> None:
#         """Create a Signal object.

#         :param pin_obj: Existing Pin object.
#         :param invert: If True, the signal will be inverted (active low).
#         """
#         ...

#     def value(self, x: Optional[bool]) -> None:
#         """This method allows to set and get the value of the signal, depending
#         on whether the argument x is supplied or not.

#         If the argument is omitted then this method gets the signal level, 1
#         meaning signal is asserted (active) and 0 - signal inactive.

#         If the argument is supplied then this method sets the signal level.
#         The argument x can be anything that converts to a boolean. If it
#         converts to True, the signal is active, otherwise it is inactive.

#         Correspondence between signal being active and actual logic level
#         on the underlying pin depends on whether signal is inverted
#         (active-low) or not. For non-inverted signal, active status
#         corresponds to logical 1, inactive - to logical 0. For
#         inverted/active-low signal, active status corresponds to
#         logical 0, while inactive - to logical 1.

#         :param x: Signal level (active or not).
#         :return: Signal level.
#         :rtype: int
#         """
#         ...

#     def on(self) -> None:
#         """Activate signal."""
#         ...

#     def off(self) -> None:
#         """Deactivate signal."""
#         ...


class UART(object):
    def __init__(self, id: int, baudrate: int = 115200) -> None:
        """Init UART object with a given baudrate.

        :param id: ID of UART "object" (either 0 or 1).
        :param baudrate: Rate of data transfer.
        """

    def init(self, baudrate: int, bits: int = 8, parity: Optional[int] = 0, stop: int = 1,
             timeout: int = 0, timeout_char: int = 0) -> None:
        """Init with a given parameters.

        :param baudrate: Baud rate, that specifies how fast data is sent over serial line.
        :param bits: Bit length of data packet (can be 7, 8 or 9 depending on parity).
        :param parity: Number of parity bits (can be 0 or 1).
        :param stop: Length of stop bit (can be 1 or 2).
        :param timeout: Timeout waiting for first char (in ms).
        :param timeout_char: Timeout waiting between chars (in ms).
        """
        ...

    def deinit(self) -> None:
        """Turn off the UART bus."""
        ...

    def any(self) -> int:
        """Returns an integer counting the number of characters that can be read
        without blocking. It will return 0 if there are no characters
        available and a positive number if there are characters. The method
        may return 1 even if there is more than one character available for reading.

        :return: Number of characters that can be read without blocking.
        """
        ...

    def read(self, nbytes: Optional[int] = None) -> bytes:
        """Read characters. If ``nbytes`` is specified then read at most that many
        bytes, otherwise read as much data as possible.

        :param nbytes: Upper limit on number of read characters.
        :return: Bytes read in.
        """
        ...

    def readinto(self, buf: bytearray, nbytes: Optional[int]) -> Optional[int]:
        """Read bytes into the ``buf``. If ``nbytes`` is specified then read at most
        that many bytes. Otherwise, read at most ``len(buf)`` bytes.

        :param buf: Buffer for holding read data.
        :param nbytes: Upper limit on number of read characters.
        :return: Number of bytes read in.
        """
        ...

    def readline(self) -> Optional[bytes]:
        """Read a line, ending in a newline character.

        :return: The line read or ``None`` on timeout.
        """
        ...

    def write(self, buf: bytearray) -> Optional[int]:
        """
        Write the buffer of bytes to the bus.

        :param buf: Data that needs to be written.
        :return: Number of bytes written or ``None`` on timeout.
        """
        ...

    def sendbreak(self) -> None:
        """
        Send a break condition on the bus. This drives the bus low for a
        duration longer than required for a normal transmission of a character.
        """


class SPI(object):

    LSB = ...  # type: int
    MSB = ...  # type: int

    def __init__(self, id: int, baudrate: int = 1000000, polarity: int = 0, phase: int = 0,
             bits: int = 8, firstbit: int = MSB, sck: Optional[Pin] = None,
             mosi: Optional[Pin] = None, miso: Optional[Pin] = None) -> None:
        """
        Construct an SPI object on the given bus, ``id``. Values of id depend
        on a particular port and its hardware. Values 0, 1, etc. are commonly
        used to select hardware SPI block #0, #1, etc. Value -1 can be used
        for bitbanging (software) implementation of SPI (if supported by a port).

        With no additional parameters, the SPI object is created but not
        initialised (it has the settings from the last initialisation of
        the bus, if any). If extra arguments are given, the bus is
        initialised. See init for parameters of initialisation.

        :param id: Bus ID.
        """
        ...

    def init(self, baudrate: int = 1000000, polarity: int = 0, phase: int = 0,
             bits: int = 8, firstbit: int = MSB, sck: Optional[Pin] = None,
             mosi: Optional[Pin] = None, miso: Optional[Pin] = None) -> None:
        """
        Initialise the SPI bus with the given parameters.

        :param baudrate: SCK clock rate.
        :param polarity: Level the idle clock line sits at (0 or 1).
        :param phase: Sample data on the first or second clock edge respectively (0 or 1).
        :param bits: Width in bits of each transfer.
        :param firstbit: Can be ``SPI.MSB`` or ``SPI.LSB``.
        :param sck: SCK pin.
        :param mosi: MOSI pin.
        :param miso: MISO pin.
        """
        ...

    def deinit(self) -> None:
        """Turn off the SPI bus."""
        ...

    def read(self, nbytes: int, write: int = 0x00) -> bytes:
        """Read a number of bytes specified by ``nbytes`` while continuously
        writing the single byte given by ``write``. Returns a ``bytes``
        object with the data that was read.

        :param nbytes: Number of characters to read.
        :param write: Value to continiously write while reading data.
        :return: Bytes read in.
        """
        ...

    def readinto(self, buf: bytearray, write: int = 0x00) -> None:
        """Read into the buffer specified by ``buf`` while continuously writing
        the single byte given by ``write``.
        """
        ...

    def write(self, buf: bytes) -> None:
        """Write the bytes contained in ``buf``.

        :param buf: Bytes to write.
        """
        ...

    def write_readinto(self, write_buf: bytearray, read_buf: bytearray) -> None:
        """Write the bytes from ``write_buf`` while reading into ``read_buf``. The
        buffers can be the same or different, but both buffers must have
        the same length.

        :param write_buf: Buffer to read data into.
        :param read_buf: Buffer to write data from.
        """
        ...


class I2C(object):
    def __init__(self, id: int, scl: Pin = None, sda: Pin = None, freq: int = 400000) -> None:
        """Construct and return a new I2C object.

        :param id: Particular I2C peripheral (-1 for software implementation).
        :param scl: Pin object specifying the pin to use for SCL.
        :param sda: Pin object specifying the pin to use for SDA.
        :param freq: Maximum frequency for SCL.
        """
        ...

    def init(self, scl: Pin, sda: Pin, *, freq: int = 400000) -> None:
        """
        Initialise the I2C bus with the given arguments.

        :param scl: Pin object specifying the pin to use for SCL.
        :param sda: Pin object specifying the pin to use for SDA.
        :param freq: Maximum frequency for SCL.
        """
        ...

    def scan(self) -> Collection[int]:
        """Scan all I2C addresses between *0x08* and *0x77* inclusive and return a
        list of those that respond. A device responds if it pulls the SDA
        line low after its address (including a write bit) is sent on the bus.
        """
        ...

    def start(self) -> None:
        """Generate a START condition on the bus (SDA transitions to low while SCL is high)."""
        ...

    def stop(self) -> None:
        """Generate a STOP condition on the bus (SDA transitions to high while SCL is high)."""
        ...

    def readinto(self, buf: bytearray, nack: bool = True) -> None:
        """Reads bytes from the bus and stores them into ``buf``. The number of bytes
        read is the length of ``buf``. An **ACK** will be sent on the bus after
        receiving all but the last byte. After the last byte is received,
        if ``nack`` is true then a **NACK** will be sent, otherwise an **ACK** will be
        sent (and in this case the slave assumes more bytes are going to be
        read in a later call).

        :param buf: Buffer to read bytes into.
        :param nack: If true, then NACK will be sent after reading last bytes.
        """
        ...

    def write(self, buf: bytearray) -> None:
        """Write the bytes from ``buf`` to the bus. Checks that an **ACK** is received
        after each byte and stops transmitting the remaining bytes if a
        **NACK** is received. The function returns the number of ACKs that
        were received.

        :param buf: Buffer to write bytes from.
        """

    def readfrom(self, addr: int, nbytes: int, stop: bool = True) -> bytes:
        """Read ``nbytes`` from the slave specified by ``addr``.

        :param addr: Address of slave device.
        :param nbytes: Maximum amount of bytes to be read.
        :param stop: If true, then STOP condition is generated at the end of the transfer.
        :return: Data read.
        """
        ...

    def readfrom_into(self, addr: int, buf: bytearray, stop: bool = True) -> None:
        """Read into ``buf`` from the slave specified by ``addr``. The number of
        bytes read will be the length of buf. If ``stop`` is true then a **STOP**
        condition is generated at the end of the transfer.

        :param addr: Address of slave device.
        :param buf: Buffer for storing read data.
        :param stop: If true, then STOP condition is generated at the end of the transfer.
        """
        ...

    def writeto(self, addr: int, buf: bytearray, stop: bool = True) -> None:
        """Write the bytes from ``buf`` to the slave specified by ``addr``. If a **NACK** is
        received following the write of a byte from buf then the remaining
        bytes are not sent. If stop is true then a **STOP** condition is generated
        at the end of the transfer, even if a **NACK** is received.

        :param addr: Address of slave device.
        :param buf: Buffer to write data from.
        :param stop: If true, then STOP condition is generated at the end of the transfer.
        :return: Number of ACKs that were received.
        """
        ...

    def readfrom_mem(self, addr: int, memaddr: int, addrsize: int = 8) -> bytes:
        """Read ``nbytes`` from the slave specified by ``addr`` starting from the memory
        address specified by ``memaddr``. The argument ``addrsize`` specifies the
        address size in bits. Returns a bytes object with the data read.

        :param addr: Address of slave device.
        :param memaddr: Memory address location on a slave device to read from.
        :param addrsize: Address size in bits.
        :return: Data that has been read.
        """
        ...

    def readfrom_mem_into(self, addr: int, memaddr: int, buf, *, addrsize=8) -> None:
        """Read into ``buf`` from the slave specified by addr starting from the memory
        address specified by ``memaddr``. The number of bytes read is the length
        of ``buf``. The argument ``addrsize`` specifies the address size in bits
        (on ESP8266 this argument is not recognised and the address size is
        always 8 bits).

        :param addr: Address of slave device.
        :param memaddr: Memory address location on a slave device to write into.
        :param buf: Buffer to store read data.
        :param addrsize: Address size in bits.
        """
        ...

    def writeto_mem(self, addr: int, memaddr: int, addrsize=8) -> None:
        """Write ``buf`` to the slave specified by ``addr`` starting from the
        memory address specified by ``memaddr``. The argument ``addrsize`` specifies
        the address size in bits (on ESP8266 this argument is not recognised
        and the address size is always 8 bits).

        :param addr: Address of slave device.
        :param memaddr: Memory address location on a slave device to write into.
        :param addrsize: Address size in bits.
        """
        ...


class RTC(object):
    def __init__(self, id: int = 0) -> None:
        """Create an RTC object.

        :param id: ID of RTC device.
        """
        ...

    def init(self, datetime: tuple) -> None:
        """Initialise the RTC. Datetime is a tuple of the form:

        ``(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])``

        :param datetime: Tuple with information regarding desired initial date.
        """
        ...

    def now(self) -> tuple:
        """Get get the current datetime tuple.

        :return: Current datetime tuple.
        """
        ...

    def deinit(self) -> None:
        """Resets the RTC to the time of January 1, 2015 and starts running it again."""
        ...

    def alarm(self, id: int, time: Union[int, tuple], *, repeat: bool = False) -> None:
        """Set the RTC alarm. Time might be either a millisecond value to program the
        alarm to current ``time + time_in_ms`` in the future, or a ``datetimetuple``.
        If the ``time`` passed is in milliseconds, repeat can be set to True to
        make the alarm periodic.

        :param id: Alarm ID.
        :param time: Either timestamp in milliseconds or datetime tuple, describing desired moment in the future.
        :param repeat: Make alarm periodic, if time passed as milliseconds.
        """
        ...

    def alarm_left(self, alarm_id: int = 0) -> int:
        """
        Get the number of milliseconds left before the alarm expires.

        :param alarm_id: Alarm ID.
        :return: Tumber of milliseconds left before the alarm expires.
        :rtype: int
        """
        ...

    def cancel(self, alarm_id: int = 0) -> None:
        """
        Cancel a running alarm.

        :param alarm_id: Alarm ID.
        """
        ...

    def irq(self, *, trigger: int, handler: Callable = None, wake: int = IDLE) -> None:
        """
        Create an irq object triggered by a real time clock alarm.

        :param trigger: Must be ``RTC.ALARM0``.
        :param handler: Function to be called when the callback is triggered.
        :param wake: Sleep mode from where this interrupt can wake up the system.
        """
        ...

    ALARM0 = ...  # type: int


class Timer(object):
    ONE_SHOT = ...  # type: int
    PERIODIC = ...  # type: int

    def __init__(self, id: int) -> None:
        """
        Construct a new timer object of the given id. Id of -1 constructs a
        virtual timer (if supported by a board).

        :param id: Timer ID.
        """

    def init(self, mode : Timer.PERIODIC, period : int, callback : func) -> None:
        """
        Init the timer. Start the timer, and enable the timer peripheral.
        """
        ...

    def deinit(self) -> None:
        """
        Deinitialises the timer. Stops the timer, and disables the timer peripheral.
        """
        ...

class ADC(object):
    """
    - id：使用的 ADC 设备编号，id = 1 表示编号为 1 的 ADC 设备;
    - channel：使用的 ADC 设备通道号，每个 ADC 设备对应多个通道;
    - 例如：ADC(1,4) 表示当前使用编号为 1 的 ADC 设备的 4 通道;
    """

    def __init__(self, id: int, channel: int) -> None:
        """
        """

    def init(self, channel : int) -> None:
        """
        根据输入的层参数初始化 ADC 对象，入参为使用的 ADC 对象通道号；
        """
        ...

    def deinit(self) -> None:
        """
        用于关闭 ADC 对象，ADC 对象 deinit 之后需要重新 init 才能使用。
        """
        ...

    def read(self) -> None:
        """
        用于获取并返回当前 ADC 对象的采样值。例如当前采样值为 2048，对应设备的分辨率为 12位，当前设备参考电压为 3.3V ，则该 ADC 对象通道上实际电压值的计算公式为：采样值 * 参考电压  /  （1 <<  分辨率位数），即 vol = 2048 / 4096 * 3.3 V = 1.15V。
        """
        ...

class PWM(object):
    """
    在给定的总线上构建一个 PWM 对象，参数介绍如下：

    - id：使用的 PWM 设备编号，如  id = 1 表示编号为 1 的 PWM 设备；
    - channel：使用的 PWM 设备通道号，每个 PWM 设备包含多个通道，范围为 [0, 4]；
    - freq：初始化频率，范围 [1, 156250]；
    - duty：初始化占空比数值，范围 [0 255]；

    例如：PWM(1,4,100,100) 表示当前使用 编号为 1 的 PWM 设备的 4 通道，初始化频率为 1000 Hz，初始化占空比的数值为 100。
    """

    def __init__(self, id: int, channel: int, freq: int, duty: int) -> None:
        """
        """

    def init(self, channel : int, freq : int, duty : int) -> None:
        """
        根据输入的参数初始化 PWM 对象。
        """
        ...

    def deinit(self) -> None:
        """
        用于关闭 PWM 对象，对象 deinit 之后需要重新 init 才能使用。
        """
        ...

    def freq(self, freq : int = None)-> None:
        """
        用于获取或者设置 PWM 对象的频率，频率的范围为 [1, 156250]。如果参数为空，返回当前 PWM 对象的频率；如果参数非空，则使用该参数设置当前 PWM 对象的频率。
        """
        ...

    def duty(self, duty : int = None) -> None:
        """
        用于获取或者设置 PWM 对象的占空比数值，占空比数值的范围为 [0, 255]，例如 duty = 100，表示当前设备占空比为 100/255 = 39.22% 。如果参数为空，返回当前 PWM 对象的占空比数值；如果参数非空，则使用该参数设置当前 PWM 对象的占空比数值。
        """
        ...

class LCD(object):
    """
    在给定总线上构造一个 LCD 对象，无入参，初始化的对象取决于特定硬件。
    """

    WHITE = ...  # type: int
    BLACK = ...  # type: int 
    BLUE  = ...  # type: int
    BRED  = ...  # type: int
    GRED  = ...  # type: int
    GBLUE  = ...  # type: int
    RED  = ...  # type: int
    MAGENTA  = ...  # type: int
    GREEN  = ...  # type: int
    CYAN  = ...  # type: int
    YELLOW  = ...  # type: int
    BROWN  = ...  # type: int
    BRRED  = ...  # type: int
    GRAY = ...  # type: int 
    GRAY175 = ...  # type: int 
    GRAY151  = ...  # type: int
    GRAY240 = ...  # type: int

    def __init__(self) -> None:
        """
        """

    def light(self, value : int) -> None:
        """
        控制是否开启 LCD 背光，入参为 True 则打开 LCD 背光，入参为 False 则关闭 LCD 背光。
        """
        ...

    def fill(self, color : int) -> None:
        """
        根据给定的颜色填充整个屏幕，支持多种颜色，可以传入的参数有：

        - WHITE BLACK BLUE BRED GRED GBLUE RED MAGENTA GREEN CYAN YELLOW BROWN BRRED GRAY GRAY175 GRAY151 GRAY240
        """
        ...

    def pixel(self, x : int, y : int , color : int) -> None:
        """
        向指定的位置（x, y）画点，点的颜色为 color 指定的颜色，可指定的颜色和上一个功能相同。
        注意：(x, y)  坐标的范围是 0 - 239，使用下面的方法对坐标进行操作时同样需要遵循此限制。
        """
        ...

    def set_color(self, back_color : int, fore_color : int) -> None:
        """
        设置 LCD 屏幕的前景色和背景色。
        """
        ...


    def text(self, input_str : str, x : int, y : int, size : int) -> None:
        """
        在指定的位置（x,y）写入字符串，字符串由 str 指定，字体的大小由 size 指定，size 的大小可为 16，24，32。
        """
        ...

    def line(self, x1 : int, y1 : int, x2 : int, y2 : int) -> None:
        """
        在 LCD 上画一条直线，起始地址为 （x1, y1），终点为（x2, y2）。
        """
        ...

    def rectangle(self, x1 : int, y1 : int, x2 : int, y2 : int) -> None:
        """
        在 LCD 上画一个矩形，左上角的位置为（x1, y1），右下角的位置为（x2, y2）。
        """
        ...

    def circle(self, x1 : int, y1 : int, r : int) -> None:
        """
        在 LCD 上画一个圆形，圆心的位置为（x1, y1），半径长度为 r。
        """
        ...

    def show_image(self, x : int, y : int, length : int, wide : int, data : bytes) -> None:
        """
        在 LCD 指定位置上显示以字节码方式存储的图片信息。
        """
        ...

    def show_bmp(self, x: int, y: int, pathname: str) -> None:
        """
        在 LCD 指定位置上显示 bmp 格式的图片信息，注意显示 bmp 图片时，(x, y) 坐标是图片的左下角。
        """
        ...

class WDT(object):

    def __init__(self, timeout : int) -> None:
        """
        Construct a new watchdog object.
        """

    def feed(self) -> None:
        """
        Perform the dog feed operation and clear the watchdog counter.
        """
        ...

def reset() -> None:
    """Resets the device in a manner similar to pushing the external RESET button."""
    ...

def reset_cause() -> int:
    """Get the reset cause. Below are possible return values:

    * ``machine.PWRON_RESET``
    * ``machine.HARD_RESET``
    * ``machine.WDT_RESET``
    * ``machine.DEEPSLEEP_RESET``
    * ``machine.SOFT_RESET``

    :return: Reset cause.
    :rtype: int
    """
    ...

def disable_irq() -> int:
    """Disable interrupt requests. Returns the previous IRQ state which should
    be considered an opaque value. This return value should be passed to
    the ``enable_irq`` function to restore interrupts to their original state,
    before ``disable_irq`` was called.

    :return: Previous IRQ state.
    :rtype: int
    """
    ...

def enable_irq(state: int) -> None:
    """Re-enable interrupt requests. The state parameter should be the value
    that was returned from the most recent call to the ``disable_irq`` function.

    :param state: IRQ state, previously returned from ``disable_irq`` function.
    """
    ...

def freq() -> int:
    """
    Returns CPU frequency in hertz.

    :return: CPU frequency in hertz.
    """

def idle() -> None:
    """Gates the clock to the CPU, useful to reduce power consumption at any time
    during short or long periods. Peripherals continue working and execution
    resumes as soon as any interrupt is triggered (on many ports this includes
    system timer interrupt occurring at regular intervals on the order of millisecond).
    """

def sleep() -> None:
    """Stops the CPU and disables all peripherals except for WLAN. Execution is
    resumed from the point where the sleep was requested. For wake up to
    actually happen, wake sources should be configured first.
    """

def deepsleep() -> None:
    """Stops the CPU and all peripherals (including networking interfaces, if
    any). Execution is resumed from the main script, just as with a reset.
    The reset cause can be checked to know that we are coming from
    ``machine.DEEPSLEEP``. For wake up to actually happen, wake
    sources should be configured first, like Pin change or RTC timeout.
    """

def wake_reason() -> int:
    """Get the wake reason. Possible values are:

    * ``machine.WLAN_WAKE``
    * ``machine.PIN_WAKE``
    * ``machine.RTC_WAKE``

    :return: Wake reason.
    """
    ...

def unique_id() -> bytearray:
    """
    Returns a byte string with a unique identifier of a board/SoC. It will
    vary from a board/SoC instance to another, if underlying hardware allows.
    Length varies by hardware (so use substring of a full value if you expect
    a short ID). In some MicroPython ports, ID corresponds to the network MAC address.
    :return: Unique identifier of a board/SoC.
    """
    ...

def time_pulse_us(pin: Pin, pulse_level: int, timeout_us: int = 1000000) -> int:
    """
    Time a pulse on the given pin, and return the duration of the pulse in
    microseconds. The pulse_level argument should be 0 to time a low pulse
    or 1 to time a high pulse.

    If the current input value of the pin is different to pulse_level, the
    function first (*) waits until the pin input becomes equal to pulse_level,
    then (**) times the duration that the pin is equal to pulse_level. If the
    pin is already equal to pulse_level then timing starts straight away.

    The function will return **-2** if there was timeout waiting for condition marked
    (*) above, and **-1** if there was timeout during the main measurement, marked (**)
    above. The timeout is the same for both cases and given by timeout_us
    (which is in microseconds).

    :param pin: Pin for timing a pulse on.
    :param pulse_level: Level of pulse (*1* for high, *0* for low)
    :param timeout_us: Duration of wait for pin change conditions, in microsecond.
    :return: Result code (-1 or -2)
    """
    ...

