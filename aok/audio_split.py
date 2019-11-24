from aok.util import Util

import click
from pydub import AudioSegment

class AudioSplit():
    """A structure to split an audio file.
    """
    def __init__(self, song: click.File, format: str) -> None:
        """Prepares an audio container to store and split an audio file.

        Parameters
        ----------
        song
            the audio file to split
        format
            the audio file's format
        """
        self._split_song = AudioSegment.empty()
        self._song = song
        self._format = format or 'mp3'

    @staticmethod
    def split_song(song: click.File, format: str, seconds: int) -> AudioSegment:
        """Split a given song for given number of seconds.

        Parameters
        ----------
        song
            the song to split
        format
            the song's file format
        seconds
            the number of seconds to split from the song

        Returns
        -------
            a song split for given seconds
        """
        return AudioSplit(song, format).split(seconds)

    def split(self, seconds: int) -> AudioSegment:
        """Split the audio segment for given number of seconds.

        Parameters
        ----------
        seconds
            the number of seconds to split a given song

        Returns
        -------
            the song split for given number of seconds
        """
        milli_seconds = Util.get_milliseconds(seconds)
        loaded_song = AudioSegment.from_file(self._song, format=self._format)
        actual_milli_seconds = len(loaded_song)

        if milli_seconds <= actual_milli_seconds:
            self._split_song = loaded_song[:milli_seconds]
        else:
            click.secho('The length specified is is greater than actual song\'s length.\n'
             + 'Exporting the actual song instead.',
                fg='yellow', bold=True)
            self._split_song = loaded_song

        return self._split_song
