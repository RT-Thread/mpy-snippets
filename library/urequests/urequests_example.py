
try:
    import urequests as requests
except ImportError:
    import requests

r = requests.get("http://www.baidu.com/")
print(r)
print(r.content)
r.close()