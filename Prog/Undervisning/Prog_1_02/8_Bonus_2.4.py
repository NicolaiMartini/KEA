from machine import Pin
from buzzer_music import music
from time import sleep

"""
Find a piece of music on onlinesequencer.net, click edit,
then select all notes with CTRL+A and copy them with CTRL+C

Paste string as shown below after removing ";:" from
the end and "Online Sequencer:120233:" from the start
"""
#    https://onlinesequencer.net/1864297 - Tetris
song = '0 E6 1 1;4 B5 1 1;6 C6 1 1;8 D6 1 1;10 E6 1 1;11 D6 1 1;12 C6 1 1;14 B5 1 1;16 A5 1 1;20 A5 1 1;22 C6 1 1;24 E6 1 1;28 D6 1 1;30 C6 1 1;32 B5 1 1;36 B5 1 1;36 B5 1 1;38 C6 1 1;40 D6 1 1;44 E6 1 1;48 C6 1 1;52 A5 1 1;56 A5 1 1'
#    https://onlinesequencer.net/358271 - LotR
#song2 = '0 F5 1 4;3 E5 1 4;7 D5 1 4;13 C5 1 4;17 C5 1 4;18 C5 1 4;20 D5 1 4;26 D5 1 4;31 G5 1 4;33 A5 1 4;35 A#5 1 4;39 A5 1 4;41 G5 1 4;43 F5 1 4;47 G5 1 4;49 A5 1 4;51 G5 1 4'


mySong = music(song, pins=[Pin(14)], tempo=3) # song 1
while True:
    print(mySong.tick())
    sleep(0.04)

PB1 = Pin(4,Pin.IN)
LED_RED = Pin(26,Pin.OUT)
LED_RED.on()
LED_YELLOW = Pin(12,Pin.OUT)
LED_YELLOW.on()
LED_GREEN = Pin(13,Pin.OUT)
LED_GREEN.off()
while True:
    LED_YELLOW.off()
    LED_GREEN.off()

    first=PB1.value()
    sleep(0.01)
    second=PB1.value()
    if first==1 and second==0:
        count+=1
    if count==2:
        LED_GREEN.on()
        LED_YELLOW.on()
        print("Song 2 is now playing.")
        mySong2 = music(song2, pins=[Pin(14)], tempo=3)# song 2
        print(mySong2.tick())
        sleep(0.04)
     first=PB1.value()
     sleep(0.01)
     second=PB1.value()
     if first==1 and second==0:
         count=1