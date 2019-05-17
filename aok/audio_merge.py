from datetime import datetime

from pydub import AudioSegment

class AudioMerge():
    """A structure to handle audio file merges.
    """
    def __init__(self, songs):
        self._playlist = AudioSegment.empty()
        self._songs = songs
    
    def merge(self):
        """Concats input audio files.
        """
        for song in self._songs:
            self._playlist += AudioSegment.from_file(song)

    def export(self, path):
        """Exports playlist to the path specified.

        If no path is present, a temporary file is generated in current directory.
        """
        self._playlist.export(path if path else 'playlist{0}.mp3'.format(datetime.now().strftime('%Y%m%d%H%M%S')))