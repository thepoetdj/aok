from datetime import datetime
from typing import Sequence

import click
from pydub import AudioSegment

class AudioMerge():
    """A structure to handle audio file merges.
    """
    def __init__(self, songs: Sequence[click.File]) -> None:
        """Generates an empty playlist to append the songs to.

        Parameters
        ----------
        songs
            the AudioSegments to append to the playlist
        """
        self._playlist = AudioSegment.empty()
        self._songs = songs
    
    @staticmethod
    def merge_all(songs: Sequence[click.File]) -> AudioSegment:
        """Provides a handle to the concatenated playlist.

        Parameters
        ----------
        songs
            the AudioSegments to join
        
        Returns
        -------
            a concatenated playlist
        """
        return AudioMerge(songs).merge()

    def merge(self) -> AudioSegment:
        """Concats input audio files.

        Repeats the audio when only single file is provided.

        Returns
        -------
            a concatenated playlist
        """
        if len(self._songs) == 1:
            self._playlist = AudioSegment.from_file(self._songs[0]) * 2
        else:
            for song in self._songs:
                self._playlist += AudioSegment.from_file(song)
        
        return self._playlist
