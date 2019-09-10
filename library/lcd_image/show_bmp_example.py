from machine import LCD
from lcd_bmp import lcd_bmp_show

def main():
    lcd = LCD()
    lcd.light(True)
    lcd.set_color(lcd.WHITE, lcd.BLACK)
    # bmp_show(lcd, 10, 240, "damao.bmp")
    lcd_bmp_show(lcd, 10, 240, "sun.bmp")

if __name__ == '__main__':
    main()