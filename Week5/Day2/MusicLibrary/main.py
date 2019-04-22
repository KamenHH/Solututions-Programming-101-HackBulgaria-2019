from playlist import Playlist
from music_crawler import MusicCrawler


MUSIC_DIR = 'Music' #  to be overriden if a different directory is going to be crawled

def main():
    crawler = MusicCrawler(MUSIC_DIR)
    songs_data = crawler.generate_songs()
    pl = Playlist('Playlist1')
    pl.add_songs(songs_data)
    pl.pprint_playlist()


if __name__ == "__main__":
    main()