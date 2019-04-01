from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
import mutagen

song = MP3('Music/Van Halen - Panama.mp3')
[print(k, v) for k, v in song.__dict__.items()]
# print(dir(song))