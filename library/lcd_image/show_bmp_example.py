from machine import LCD

# Currently only supports 32-bit BMP true color image display

def main():
    lcd = LCD()
    lcd.light(True)
    lcd.set_color(lcd.WHITE, lcd.BLACK)
    lcd.show_bmp(180, 50, "sun.bmp")

if __name__ == '__main__':
    main()
