import machine
import rtthread

rtthread.wifi_join("w0", "test", "123456789")

player = machine.Player()
player.opensong("http://music.163.com/song/media/outer/url?id=447925558.mp3")
player.set_volume(80)
player.play()
# player.pause()
