from player import player
import rtthread

rtthread.wifi_join("w0", "test", "123456789")

play = player()
play.opensong("http://music.163.com/song/media/outer/url?id=447925558.mp3")
play.play()

# play.set_volume(60)
# play.pause()
# play.stop()
