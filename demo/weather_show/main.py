import time
import network
import ujson as json
from machine import LCD
from lcd_bmp import lcd_bmp_show
from lcd_bmp import show_image_file
import urequests as requests

def lcd_init():
    lcd = LCD()                            # Create a LCD object
    lcd.light(True)                        # Open the backlight
    lcd.set_color(lcd.WHITE, lcd.BLACK)    # Set background color and foreground color
    lcd.fill(lcd.WHITE)                    # Fill the entire LCD with white
    lcd.text("City: ",     10, 105, 24)    # prints the string at 32 font size at position (0, 48)
    lcd.text("Humidity: ", 10, 135, 24)
    lcd.text("Temp: ",     10, 165, 24)

    show_image_file(lcd, 45, 45, 152, 48, "pictures/weather.img")
    show_image_file(lcd, 5, 210, 230, 29, "pictures/rt_thread_micropython.img")
    return lcd

def wifi_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)

    print("Begin to connect wifi...")
    wlan.connect(ssid, password)

    if wlan.isconnected():
        print("Wifi connect successful, waitting to get IP...")
    else:
        print("Wifi connect failed.")

    time.sleep(3)  # waitting to get IP

def main():
    ssid     = "test"
    password = "123456789"

    lcd = lcd_init()
    lcd.text("wifi connecting...", 10, 0, 24) 
    lcd.line(0, 25, 239, 25)
    wifi_connect(ssid, password)   
    lcd.text("wifi connected    ", 10, 0, 24) 
    lcd_bmp_show(lcd, 210, 20, "pictures/wifi_connect.bmp")

    # you can find cityid on this page: 
    # https://gitee.com/wangjins/weather_api/blob/master/city.json
    cityid = "101020100"  
    url = "http://www.tianqiapi.com/api/?version=v6&cityid=" + cityid + "&appid=65251531&appsecret=Yl2bzCYb"

    r = requests.get(url)
    data = json.loads(r.content.decode())

    lcd.text("City: ShangHai",                10, 105, 24)     # prints the string at 32 font size at position (0, 48)
    lcd.text("humidity: %s"%data["humidity"], 10, 135, 24)
    lcd.text("temp: %s - %s"%(data["tem2"], data["tem1"]), 10, 165, 24)
    image = "pictures/" + data["wea_img"] + ".img"                  # (xue, lei, shachen, wu, bingbao, yun, yu, yin, qing)
    show_image_file(lcd, 190, 135, 32, 32, image)
    lcd.text("wifi connected  ", 10, 0, 24) 

if __name__ == "__main__":
    main()
