from struct import *


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

    count = 0
    length = biWidth

    image_buf = bytearray(2 * biWidth)
    bmp_data_row = []

    for height in range(biHeight):
        index = 0

        bmp_data_row.clear()

        for width in range(biWidth):
            bmp_data_row.append([unpack("<B", file.read(1))[0], unpack("<B", file.read(1))[
                                0], unpack("<B", file.read(1))[0], unpack("<B", file.read(1))[0]])
            count = count + 4

        # bmp Four-byte alignment
        while count % 4 != 0:
            file.read(1)
            count = count + 1
            print("not allien")

        for rgb in bmp_data_row:
            rgb_16 = ((rgb[2] >> 3) & 0x1f) << 11 | (
                (rgb[1] >> 2) & 0x3f) << 5 | ((rgb[0] >> 3) & 0x1f)

            image_buf[index] = (rgb_16 >> 8)
            image_buf[index + 1] = rgb_16 & 0xff

            index += 2

        lcd.show_image(x, y, length, 1, image_buf)  # x, y, length, wide
        y -= 1

    file.close()
