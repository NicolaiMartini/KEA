from buzzer_music import music
from time import sleep

#Example

song = '0 C5 1 8;2 D5 1 8;4 E5 1 8;8 G5 1 8;12 E5 1 8;16 D5 1 8;20 C5 1 8;32 E5 1 8;34 G5 1 8;36 A5 1 8;40 C6 1 8;44 B5 1 8;48 G5 1 8;52 E5 1 8;56 F5 1 8;58 E5 1 8;60 D5 1 8;28 G4 1 8;62 C5 1 8;64 D5 1 8;66 E5 1 8;70 G5 1 8;74 E5 1 8;78 D5 1 8;82 C5 1 8;94 E5 1 8;96 G5 1 8;98 A5 1 8;102 C6 1 8;106 B5 1 8;110 G5 1 8;114 E5 1 8;118 F5 1 8;120 E5 1 8;122 D5 1 8;90 G4 1 8;124 C5 1 8;126 D5 1 8;128 E5 1 8;132 G5 1 8;136 E5 1 8;140 D5 1 8;144 C5 1 8;156 E5 1 8;158 G5 1 8;160 A5 1 8;164 C6 1 8;168 B5 1 8;172 G5 1 8;176 E5 1 8;180 F5 1 8;182 E5 1 8;184 D5 1 8;152 G4 1 8'

"""
Find a piece of music on onlinesequencer.net, click edit,
then select all notes with CTRL+A and copy them with CTRL+C

Paste string as shown above after removing ";:" from
the end and "Online Sequencer:120233:" from the start
"""

from machine import Pin

#HUSK AT FORBINDE MED DUPONT KABEL:
# JP6 GP6
# JP1 SCK

#One buzzer on pin 14
mySong = music(song, pins=[Pin(14)], tempo=3)

#Four buzzers
#mySong = music(song, pins=[Pin(0),Pin(1),Pin(2),Pin(3)])

while True:
    print(mySong.tick())
    sleep(0.04)

