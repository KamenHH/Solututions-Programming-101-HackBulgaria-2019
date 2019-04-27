from mutagen.mp3 import EasyMP3


class SongParser(EasyMP3):
    def __init__(self, path):
        super().__init__(path)

    def parse_song_tags(self):
        title = self.parse_title()
        artist = self.parse_artist()
        album = self.parse_album()
        length = self.parse_length()
        return (title, artist, album, length)

    def parse_title(self):
        title = self.get('title')
        return title[0] if title else 'Unknown'

    def parse_artist(self):
        artist = self.get('artist')
        return artist[0] if artist else 'Unknown'

    def parse_album(self):
        album = self.get('album')
        return album[0] if album else 'Unknown'
    
    def parse_length(self):
        return int(self.info.length)