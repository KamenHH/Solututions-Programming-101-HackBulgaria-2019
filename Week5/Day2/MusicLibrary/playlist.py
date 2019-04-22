import os
import sys
import json
import random 
from song import Song

class Playlist:
    PLAYLISTS_DIR = 'playlist-data'
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
            # slef._index = 0 IF self._repeat ELSE <no change> ?
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
        """Mutator: Shuffles the playlist in place."""
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
        
    def serialize(self):
        serialized_songs = []
        for song in self:
            serialized_songs.append({
                'title': song.title,
                'artist': song.artist,
                'album': song.album,
                'length': int(song.length(seconds=True))
            })
        return serialized_songs

    def save(self):
        """Saves the playlist instance in a new file json with the same name of the playlist."""
        filename = self._name
        if Playlist.check_filename(filename):
            with open(os.path.join(Playlist.PLAYLISTS_DIR, filename), 'w') as f:
                json.dump(self.serialize(), f, indent=4)
        

    @classmethod
    def load(cls, filename):
        try:
            f = open(os.path.join(cls.PLAYLISTS_DIR, filename))
            playlist_data = json.load(f)
            p = cls('name')
            p.add_songs(cls.deserialize(playlist_data))
            f.close()
            return p
        except FileNotFoundError:
            print(f'Playlist doesn\'t exit in "{cls.PLAYLISTS_DIR }" directory!')
            sys.exit() 

    @staticmethod
    def deserialize(playlist_data):
        deserialized_songs = []
        for song in playlist_data:
            deserialized_songs.append(Song(song["title"], song["artist"], 
                                           song["album"], song["length"]))
        return deserialized_songs
        

    @staticmethod
    def check_filename(filename):
        dir_content = os.listdir(Playlist.PLAYLISTS_DIR)
        if filename in dir_content:
            while True:
                user_input = input(f'A playlist with the name "{filename}" already exists, do you wish do override it? (Y/n)')
                if user_input.lower() == 'y':
                    return True
                elif user_input.lower() == 'n':
                    return False
        return True