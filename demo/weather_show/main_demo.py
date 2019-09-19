import time
import network
import ujson as json
from machine import LCD
import urequests as requests

def lcd_init():
    lcd = LCD()                            # Create a LCD object
    lcd.light(True)                        # Open the backlight
    lcd.set_color(lcd.WHITE, lcd.BLACK)    # Set background color and foreground color
    lcd.fill(lcd.WHITE)                    # Fill the entire LCD with white
    lcd.text("0000-00-00", 10, 0, 24) 
    lcd.line(0, 25, 239, 25)
    lcd.text("City: N/A",     10, 105, 24)    # prints the string at 32 font size at position (0, 48)
    lcd.text("Humidity: N/A", 10, 135, 24)
    lcd.text("Temp: N/A",     10, 165, 24)

    lcd.show_bmp(45, 87, "pictures/weather.bmp")
    lcd.show_bmp(5, 238, "pictures/micropython.bmp")
    lcd.show_bmp(210, 20, "pictures/wifi_week.bmp")
    return lcd

def wifi_connect(ssid, password, lcd):
    wlan = network.WLAN(network.STA_IF)

    print("Begin to connect wifi...")
    wlan.connect(ssid, password)

    if wlan.isconnected():
        print("Wifi connect successful, waitting to get IP...")
    else:
        print("Wifi connect failed.")

    count = 0
    while count < 3:
        lcd.show_bmp(210, 20, "pictures/wifi_week.bmp")
        time.sleep(0.3)
        lcd.show_bmp(210, 20, "pictures/wifi_middle.bmp")
        time.sleep(0.3)
        lcd.show_bmp(210, 20, "pictures/wifi_strong.bmp")
        time.sleep(0.3) 
        count += 1

def main():
    ssid     = "test"
    password = "123456789"

    lcd = lcd_init()

    wifi_connect(ssid, password, lcd)   

    # you can find cityid on this page: 
    # https://gitee.com/wangjins/weather_api/blob/master/city.json
    cityid = "101020100"  
    url = "http://www.tianqiapi.com/api/?version=v6&cityid=" + cityid + "&appid=65251531&appsecret=Yl2bzCYb"

    r = requests.get(url)
    data = json.loads(r.content.decode())

    lcd.text("%s"%data["date"], 10, 0, 24) 
    lcd.text("City: ShangHai",                10, 105, 24)          # prints the string at 32 font size at position (0, 48)
    lcd.text("Humidity: %s"%data["humidity"], 10, 135, 24)
    lcd.text("Temp: %s - %s"%(data["tem2"], data["tem1"]), 10, 165, 24)
    image = "pictures/" + data["wea_img"] + ".bmp"                  # (xue, lei, shachen, wu, bingbao, yun, yu, yin, qing)
    lcd.show_bmp(190, 166, image)

if __name__ == "__main__":
    main()
