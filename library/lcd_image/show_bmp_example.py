from machine import LCD
from lcd_bmp import lcd_bmp_show
import gc

# Currently only supports 32-bit BMP true color image display

def main():
    lcd = LCD()
    lcd.light(True)
    lcd.set_color(lcd.WHITE, lcd.BLACK)
    lcd_bmp_show(lcd, 180, 50, "sun.bmp")

if __name__ == '__main__':
    main()
