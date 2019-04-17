class Song:
    def __init__(self, title, artist, album, length_in_seconds):
        self._title = title
        self._artist = artist
        self._album = album
        self._length = length_in_seconds

    def __str__(self):
        return f'{self.artist} - {self.title}, from {self.album} - {self.length()}'

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist
    
    @property
    def album(self):
        return self._album
    
    def length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return f'{self._length}'
        elif minutes:
            return f'{self._length//60}'
        elif hours:
            return f'{self._length//3600}'
        else:
            return Song.build_length_str(self._length)

    @staticmethod
    def build_length_str(length_in_seconds):
            h = length_in_seconds // 3600
            m = length_in_seconds // 60
            s = length_in_seconds % 60
            if m != 0:
                if h != 0:
                    return f'{h}:{m}:{s}'
                return f'{m}:{s}'
            return f'{s}'
