from datetime import datetime
from typing import Sequence

import click
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

class AudioMerge():
    """A structure to handle audio file merges.
    """
    def __init__(self, songs: Sequence[click.File], format: str) -> None:
        """Generates an empty playlist to append the songs to.

        Parameters
        ----------
        songs
            the AudioSegments to append to the playlist
        format
            the audio file format
        """
        self._playlist = AudioSegment.empty()
        self._songs = songs
        self._format = format or 'mp3'
    
    @staticmethod
    def merge_all(songs: Sequence[click.File], format: str) -> AudioSegment:
        """Provides a handle to the concatenated playlist.

        Parameters
        ----------
        songs
            the AudioSegments to join
        format
            the audio files' format
        
        Returns
        -------
            a concatenated playlist
        """
        return AudioMerge(songs, format).merge()

    def merge(self) -> AudioSegment:
        """Concats input audio files.

        Repeats the audio when only single file is provided.

        When the input audio do not match the format specified by the
         `-f/--format` option, an empty playlist is returned instead.

        Returns
        -------
            a concatenated playlist
        """
        try:
            if len(self._songs) == 1:
                self._playlist = AudioSegment.from_file(self._songs[0],
                format=self._format) * 2
            else:
                for song in self._songs:
                    self._playlist += AudioSegment.from_file(song,
                    format=self._format)
        except CouldntDecodeError:
            click.secho('Invalid audio format of input file', fg='red', bold=True)
        
        return self._playlist
