import os
from mutagen.mp3 import EasyMP3


MUSIC_DIR = 'Music'

class MusicCrawler:
    """Each crawler contains the path to the directory to be crawled and the specific methods.
    Current limitaions: 
     - only works mp3 files.
     - doesn't craw nested directories"""

    AUDIO_FORMATS = ['.mp3'] 
    def __init__(self, music_dir):
        self._music_dir = music_dir

    @property
    def music_dir(self):
        """Returns the absolute path representation of the directory to be crawled."""
        return os.path.abspath(self._music_dir)

    @music_dir.setter
    def music_dir(self, path):
        """Checks if the specified path is valid, if not - raises an error."""
        if not os.path.isdir(path):
            raise Exception("Directory specified not found!")
        return path

    def crawl(self):
        """Crawls the specified directory containg audiо files."""
        for file in os.listdir(self._music_dir):
            root, ext = os.path.splitext
            if ext in __class__.AUDIO_FORMATS:
                #TODO finish
                pass


def main():
    c = MusicCrawler(MUSIC_DIR)
    print(c.music_dir)

if __name__ == "__main__":
    main()