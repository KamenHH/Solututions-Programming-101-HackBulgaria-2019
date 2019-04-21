from mutagen.mp3 import EasyMP3


class SongParser(EasyMP3):
    def __init__(self, path):
        super().__init__(path)

    def parse_song(self, path):
        title = self.parse_title()
        artist = self.parse_artist()
        album = self.parse_album()
        length = self.parse_length()
        return (title, artist, album, length)

    def parse_title(self):
        #TODO: implement
        return title
        pass

    def parse_artist(self):
        #TODO: implement
        return artist
        pass

    def parse_album(self):
        #TODO: implement
        return album
        pass

    def parse_length(self):
        #TODO: implement
        return length
        pass
