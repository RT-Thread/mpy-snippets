import os
from machine import LCD

def show_image_file(lcd, x, y, img_length, img_wide, path):
    read_size = 0
    file_size = os.stat(path)[6]

    if file_size > 1024:
        read_size = img_length * 2 * 2
        img_wide = 2
    else:
        read_size = file_size

    with open(path, 'rb') as infile:
        while True:
            result = infile.read(read_size)
            if result == b'':
                break

            lcd.show_image(x, y, img_length, img_wide, result)
            y += 2

def main():

    lcd = LCD()
    lcd.light(True)
    lcd.set_color(lcd.WHITE, lcd.BLACK)
    show_image_file(lcd, 70, 70, 100, 100, "ball.img")

if __name__ == '__main__':
    main()
