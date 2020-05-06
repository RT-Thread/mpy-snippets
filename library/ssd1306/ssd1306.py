# MicroPython SSD1306 OLED driver, I2C and SPI interfaces

from micropython import const
import font


# register definitions
SET_CONTRAST = const(0x81)
SET_ENTIRE_ON = const(0xA4)
SET_NORM_INV = const(0xA6)
SET_DISP = const(0xAE)
SET_MEM_ADDR = const(0x20)
SET_COL_ADDR = const(0x21)
SET_PAGE_ADDR = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP = const(0xA0)
SET_MUX_RATIO = const(0xA8)
SET_COM_OUT_DIR = const(0xC0)
SET_DISP_OFFSET = const(0xD3)
SET_COM_PIN_CFG = const(0xDA)
SET_DISP_CLK_DIV = const(0xD5)
SET_PRECHARGE = const(0xD9)
SET_VCOM_DESEL = const(0xDB)
SET_CHARGE_PUMP = const(0x8D)

class SSD1306(object):
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00,  # off
            # address setting
            SET_MEM_ADDR,
            0x00,  # horizontal
            # resolution and layout
            SET_DISP_START_LINE | 0x00,
            SET_SEG_REMAP | 0x01,  # column addr 127 mapped to SEG0
            SET_MUX_RATIO,
            self.height - 1,
            SET_COM_OUT_DIR | 0x08,  # scan from COM[N] to COM0
            SET_DISP_OFFSET,
            0x00,
            SET_COM_PIN_CFG,
            0x02 if self.height == 32 else 0x12,
            # timing and driving scheme
            SET_DISP_CLK_DIV,
            0x80,
            SET_PRECHARGE,
            0x22 if self.external_vcc else 0xF1,
            SET_VCOM_DESEL,
            0x30,  # 0.83*Vcc
            # display
            SET_CONTRAST,
            0xFF,  # maximum
            SET_ENTIRE_ON,  # output follows RAM contents
            SET_NORM_INV,  # not inverted
            # charge pump
            SET_CHARGE_PUMP,
            0x10 if self.external_vcc else 0x14,
            SET_DISP | 0x01,
        ):  # on
            self.write_cmd(cmd)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        for i in range(8):
            self.write_cmd(0xb0+i)
            self.write_cmd(0)
            self.write_cmd(0x10)
            for j in range(128):
                self.write_data(self.buffer[j*8 + i])
            
    def draw_pixel(self,x, y, t=True):
        if(x > 127):
            return
        if(y>63):
            return
        pos = y // 8
        bx = y%8
        temp = 1<<bx
        if(t):
            self.buffer[x*8 + pos] |= temp
        else:
            self.buffer[x*8 + pos] &= (~temp)

    def show_char(self, x, y, chr, size=16):
        csize = (size//8)*(size//2) if size%8 == 0 else (size//8 + 1)*(size//2)
        chr = ord(chr) - ord(' ')
        y0=y
        temp = bytes(0)
        for i in range(csize):
            if size == 12:
                temp = font.asc2_1206[chr][i]
            elif size == 16:
                temp = font.asc2_1608[chr][i]
            elif size == 24:
                temp = font.asc2_2412[chr][i]
            else:
                return
            for j in range(8):
                if( (temp&0x80) != 0):
                    self.draw_pixel(x,y,True)
                else:
                    self.draw_pixel(x,y,False)
                temp<<=1
                y+=1
                if (y - y0) == size:
                    y=y0
                    x+=1
                    break

    def show_text(self,x,y,text,size = 16):
        for chr in text:
            self.show_char(x,y,chr,size)
            x += (size//2)

    def clear(self):
        self.buffer = bytearray(self.pages * self.width)
        self.show()

    def draw_line(self, x0,y0,x1,y1):
        if x0 == x1:
            for point in range(y0, y1):
                self.draw_pixel(x0, point)
        elif y0 == y1:
            for point in range(x0, x1):
                self.draw_pixel(point, y0)
        else:
            k = (y1-y0)/(x1-x0)
            if x0 < x1:
                for point in range(x0, x1):
                    y = int(y0 + point*k)
                    self.draw_pixel(point, y)
            else:
                for point in range(x1, x0):
                    y = int(y1 + point*k)
                    self.draw_pixel(point, y)

class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x00  # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, data):
        self.temp[0] = 0x40
        self.temp[1] = data
        self.i2c.writeto(self.addr, self.temp)

class SSD1306_SPI(SSD1306):
    def __init__(self, width, height, spi, dc, res, cs, external_vcc=False):
        self.rate = 10 * 1024 * 1024
        dc.init(dc.OUT, value=0)
        res.init(res.OUT, value=0)
        cs.init(cs.OUT, value=1)
        self.spi = spi
        self.dc = dc
        self.res = res
        self.cs = cs
        import time

        self.res(1)
        time.sleep_ms(1)
        self.res(0)
        time.sleep_ms(10)
        self.res(1)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(buf)
        self.cs(1)

