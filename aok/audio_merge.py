from datetime import datetime

from pydub import AudioSegment

class AudioMerge():
    """A structure to handle audio file merges.
    """
    def __init__(self, songs):
        self._playlist = AudioSegment.empty()
        self._songs = songs
    
    @staticmethod
    def merge_all(songs):
        return AudioMerge(songs).merge()

    def merge(self):
        """Concats input audio files.

        Repeat the audio when only single file is provided.
        """
        if len(self._songs) == 1:
            self._playlist = AudioSegment.from_file(self._songs[0]) * 2
        else:
            for song in self._songs:
                self._playlist += AudioSegment.from_file(song)
        
        return self._playlist
