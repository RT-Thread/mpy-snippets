import time
import network
from machine import LCD
import ujson as json
try:
    import urequests as requests
except ImportError:
    import requests

def lcd_init():
    lcd = LCD()                             # Create a LCD object
    lcd.light(False)                        # Close the backlight
    lcd.light(True)                         # Open the backlight
    lcd.set_color(lcd.WHITE, lcd.BLACK)     # Set background color and foreground color
    lcd.fill(lcd.WHITE)                     # Fill the entire LCD with white
    lcd.text("Weather Show", 26, 48, 32)    # prints the string at 32 font size at position (0, 48)
    lcd.text("demo", 90, 120, 32)           # prints the string at 32 font size at position (0, 48)
    return lcd

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.connect("test", "123456789")

    if wlan.isconnected():
        print("wifi connect successful")
    else:
        print("wifi connect failed")

    time.sleep(3)  # waitting to get IP

def main():

    lcd = lcd_init()
    lcd.text("wifi connecting...", 0, 0, 24) 
    wifi_connect()
    lcd.text("wifi connected    ", 0, 0, 24) 

    r = requests.get("http://www.weather.com.cn/data/cityinfo/101020100.html")
    data = json.loads(r.content.decode())
    r.close()

    data = data["weatherinfo"]
    print("%s今天的天气是%s，最低温度 %s , 最高温度 %s "%(data["city"], data["weather"], data["temp1"], data["temp2"]))

if __name__ == "__main__":
    main()
