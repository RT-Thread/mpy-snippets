from recorder import recorder
import utime as time

record = recorder()
record.start("voice.wav")
time.sleep(5)
record.stop()
