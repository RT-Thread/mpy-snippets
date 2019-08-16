
try:
    import urequests as requests
except ImportError:
    import requests

r = requests.get("http://www.rt-thread.com/service/rt-thread.txt")
print(r.content)
r.close()