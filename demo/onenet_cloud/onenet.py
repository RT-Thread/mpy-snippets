import urequests as requests
from umqtt.simple import MQTTClient
import ujson as json

class Register():
    def __init__(self, url='', title='', sn='', mac=''):
        self.url = url
        self.title = title
        self.sn = sn
        self.mac = mac
        self.sock = None
        self.tjson = {}
        self.erron = 0
        self.key = ''
        self.device_id = ''

    def regist(self):
        assert self.url is not None, "Url is not set"
        _, _, host, path = self.url.split('/', 3)
        if host == '':
            return
        device = {"mac":self.mac} if self.sn == '' else {"sn":self.sn}
        if self.title != '':
            device['title'] = self.title
        jdata = json.dumps(device)

        resp = requests.post(self.url, data=jdata)
        if resp:
            self.tjson = resp.json()
            if self.tjson['errno'] == 0:
                self.key = self.tjson['data']['key']
                self.device_id = self.tjson['data']['device_id']
            return True
        else:
            return False

class OneNetMqtt:
    failed_count = 0

    def __init__(self, client_id='', username='', password=''):
        self.server = "183.230.40.39"
        self.client_id = client_id
        self.username = username
        self.password = password
        self.topic = "topic_sub"                # 填入测试 topic
        self.mqttClient = MQTTClient(
            self.client_id, self.server, 6002, self.username, self.password)
        self.cmd_times = 0                      # publish count

    def pubData(self, value):
        jdata = json.dumps(value)
        jlen = len(jdata)
        bdata = bytearray(jlen+3)
        bdata[0] = 1                             # publish data in type of json
        bdata[1] = int(jlen / 256)               # data lenght
        bdata[2] = jlen % 256                    # data lenght
        bdata[3:jlen+4] = jdata.encode('ascii')  # json data

        try:
            # $dp 为特殊系统 topic，可以通过这个 topic 给系统推送信息,但是不能订阅这个 topic
            self.mqttClient.publish('$dp', bdata)
            self.cmd_times += 1
            self.failed_count = 0
        except Exception as ex:
            self.failed_count += 1
            print('publish failed:', ex.message())
            if self.failed_count >= 3:
                print('publish failed three times, resetting...')

    def sub_callback(self, topic, msg):
        print((topic, msg))
        cmd = msg.decode('ascii').split(" ")
        print('sub_callback : %s'%cmd)

    def connect(self):
        self.mqttClient.set_callback(self.sub_callback)
        self.mqttClient.connect()
        self.mqttClient.subscribe(self.topic)
        print("Connected to %s, subscribed to %s topic." % (self.server, self.topic))
        # try:
        #     while True:
        #         self.mqttClient.check_msg()
        # finally:
        #     self.mqttClient.disconnect()
        #     print('MQTT closed')
