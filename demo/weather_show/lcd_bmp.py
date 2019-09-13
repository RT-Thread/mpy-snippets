from struct import *
import gc

def lcd_bmp_show(lcd, x, y, filepath):
    """Displays 32-bit BMP files on LCD.

    lcd      : lcd object
    x        : image display x coordinates
    y        : image display y coordinates
    filepath : filepath to display
    """
    file = open(filepath, "rb")

    # 读取 bmp 文件的文件头 14 字节
    # 0x4d42 对应BM 表示这是Windows支持的位图格式
    bfType = unpack("<h", file.read(2))[0]
    bfSize = unpack("<i", file.read(4))[0]             # 位图文件大小
    bfReserved1 = unpack("<h", file.read(2))[0]        # 保留字段 必须设为 0
    bfReserved2 = unpack("<h", file.read(2))[0]        # 保留字段 必须设为 0
    # 偏移量 从文件头到位图数据需偏移多少字节（位图信息头、调色板长度等不是固定的，这时就需要这个参数了）
    bfOffBits = unpack("<i", file.read(4))[0]

    # 读取 bmp 文件的位图信息头 40 字节
    biSize = unpack("<i", file.read(4))[0]             # 所需要的字节数
    biWidth = unpack("<i", file.read(4))[0]            # 图像的宽度 单位 像素
    biHeight = unpack("<i", file.read(4))[0]           # 图像的高度 单位 像素
    biPlanes = unpack("<h", file.read(2))[0]           # 说明颜色平面数 总设为 1
    biBitCount = unpack("<h", file.read(2))[0]         # 说明比特数
    biCompression = unpack("<i", file.read(4))[0]      # 图像压缩的数据类型
    biSizeImage = unpack("<i", file.read(4))[0]        # 图像大小
    biXPelsPerMeter = unpack("<i", file.read(4))[0]    # 水平分辨率
    biYPelsPerMeter = unpack("<i", file.read(4))[0]    # 垂直分辨率
    biClrUsed = unpack("<i", file.read(4))[0]          # 实际使用的彩色表中的颜色索引数
    biClrImportant = unpack("<i", file.read(4))[0]     # 对图像显示有重要影响的颜色索引的数目

    if biBitCount != 32:
        print("目前只支持 32位 BMP 真彩图片显示，" + str(biBitCount) + "位图片与本程序不匹配。")

    image_buf = bytearray(2 * biWidth)
    row_buf = bytearray(4 * biWidth)

    for height in range(biHeight):
        index = 0
        rgb_index = 0

        row_buf = file.read(4 * biWidth)

        while rgb_index < (4 * biWidth):
            rgb_16 = ((row_buf[rgb_index + 2] >> 3) & 0x1f) << 11 | ((row_buf[rgb_index + 1] >> 2) & 0x3f) << 5 | ((row_buf[rgb_index] >> 3) & 0x1f)
            image_buf[index] = (rgb_16 >> 8)
            image_buf[index + 1] = rgb_16 & 0xff
            rgb_index += 4
            index += 2

        lcd.show_image(x, y, biWidth, 1, image_buf)  # x, y, length, wide

        y -= 1

        if y < 0:
            break

    file.close()
    gc.collect()

def show_image_file(lcd, x, y, img_length, img_wide, path):
    import os
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