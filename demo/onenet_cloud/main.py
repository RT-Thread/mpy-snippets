from onenet import Register, OneNetMqtt
import time
import network
from machine import I2C, Pin
from aht10 import AHT10
from machine import LCD

def lcd_init():
    lcd = LCD()                             # Create a LCD object
    lcd.light(False)                        # Close the backlight
    lcd.light(True)                         # Open the backlight
    lcd.set_color(lcd.WHITE, lcd.BLACK)     # Set background color and foreground color
    lcd.fill(lcd.WHITE)                     # Fill the entire LCD with white
    lcd.text("Onenet Cloud", 26, 48, 32)  # prints the string at 32 font size at position (0, 48)
    lcd.text("demo", 90, 120, 32)  # prints the string at 32 font size at position (0, 48)
    return lcd

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.connect("test", "123456789")

    if wlan.isconnected():
        print("wifi connect successful, waitting to get IP")
    else:
        print("wifi connect failed")

    time.sleep(3)  # waitting to get IP

def aht10_init():

    PIN_CLK = 23   # PA0, get the pin number from get_pin_number.py
    PIN_SDA = 24   # PA1

    clk = Pin(("clk", PIN_CLK), Pin.OUT_OD)   # Select the PIN_CLK as the clock
    sda = Pin(("sda", PIN_SDA), Pin.OUT_OD)   # Select the PIN_SDA as the data line

    i2c = I2C(-1, clk, sda, freq=100000)
    sensor = AHT10(i2c)
    sensor.sensor_init()
    sensor.is_calibration_enabled()

    return sensor

def main():

    lcd = lcd_init()
    lcd.text("wifi connecting...", 0, 0, 24) 
    wifi_connect()
    lcd.text("wifi connected    ", 0, 0, 24) 

    sn = 'RT_Thread_Test_Product_5'                     # 1.填入设备唯一标识符
    title = 'Device' + sn
    product_id = 'xxxxxx'                               # 2.填入创建设备时获得的产品 ID
    reg_key = 'vxwc3uy7LZsqxxx'                        # 3.填入正式环境注册码
    url = 'http://api.heclouds.com/register_de?register_code=' + reg_key

    # 4.通过设备信息注册设备，如果该设备已经注册则不再重复注册
    reg = Register(url=url, title=title, sn=sn)

    if reg.regist():
        MQTT = OneNetMqtt(client_id=reg.device_id,
                          username=product_id, password=reg.key)  # 开启 MQTT 服务
        MQTT.connect()
    else:
        print('Error: No Client ID!')

    sensor = aht10_init()
    count = 1
    while count < 6:

        temp = sensor.read_temperature()
        humi = sensor.read_humidity()

        data = {'datastreams': [
            {"id": "temp", "datapoints": [{"value": temp}]},
            {"id": "humi", "datapoints": [{"value": humi}]}
            ]}

        print("upload sensor data %d times, current temp: %.2f, humi: %.2f %%"%(count, temp, humi))
        MQTT.pubData(data)
        print(data)
        time.sleep(1)
        count += 1

    MQTT.mqttClient.disconnect()

if __name__ == "__main__":
    main()
