from song import Song
import random 

class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self._song_list = []
        self._name = name
        self._repeat = repeat
        self._shuffle = shuffle
        self._index = 0

    def __str__(self):
        return f'{self._name} - Number of songs: {len(self._song_list)}'

    def __iter__(self):
        return self

    def __next__(self):
        # next_song() method
        index = self._index
        self._index += 1
        
        try:
            return self._song_list[index]
        except IndexError:
            self._index = 0
            raise StopIteration

    def add_song(self, song):
        """Mutator: Adds a song to the playlist, song MUST be a Song instance!"""
        self._song_list.append(song)

    def remove_song(self, title):
        """Mutator: Given its title, removes a song from the playlist."""
        for song in self._song_list:
            if song.title == title:
                self._song_list.remove(song)
    
    def add_songs(self, songs):
        """Mutator: Adds N songs to the playlist where N=len(songs)."""
        for song in songs:
            self.add_song(song)

    def total_length(self):
        """Accessor: Returns the total length of the play list (sum of all the song lengths)."""
        return Song.build_length_str(sum([int(song.length(seconds=True)) for song in self._song_list]))

    def artists(self):
        """Accessor: Returns a table of <artist - corresponding number of songs>."""
        artists = {}
        for song in self._song_list:
            artists[song.artist] = artists.get(song.artist, 0) + 1
        return artists

    def shuffle_playlist(self):
        if self._shuffle:
            random.shuffle(self._song_list)

    def pprint_playlist(self):
        """Prints the playlist. Example:
        | Artist | Song | Length |
        | -------|------|--------|
        | AC/DC  | TNT  |  3:44  |"""
        artists_col_width = len(max(self._song_list, 
                                       key=lambda song: len(song.artist)).artist)
        titles_col_width = len(max(self._song_list, 
                                       key=lambda song: len(song.title)).title)
        length_col_width = len(max(self._song_list, 
                                       key=lambda song: len(song.length())).length())

        artists_col_width = max(len("Artist"), artists_col_width)
        titles_col_width = max(len("Title"), titles_col_width)
        length_col_width = max(len('Length'), length_col_width)
        
        print(f'| {"Artist".ljust(artists_col_width)} '\
              f'| {"Title".ljust(titles_col_width)} ' \
              f'| {"Length".ljust(length_col_width)} |')

        print(f'| {"-"*artists_col_width} | {"-"*titles_col_width} | {"-"*length_col_width} |')
        
        for song in self._song_list:
            print(f'| {song.artist.ljust(artists_col_width)} ' \
                  f'| {song.title.ljust(titles_col_width)} ' \
                  f'| {song.length().ljust(length_col_width)} |')


        