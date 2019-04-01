from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
import mutagen

song = mutagen.File('Music/Van Halen - Panama.mp3', easy=True)
print(song)