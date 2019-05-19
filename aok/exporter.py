from datetime import datetime

import click
from pydub import AudioSegment

class Exporter:
    @staticmethod
    def export(path: click.Path, playlist: AudioSegment) -> None:
        """Exports playlist to the path specified.

        If no path is present, a temporary file is generated in current directory.

        Parameters
        ----------
        path
            the output file path
        playlist
            the playlist to export
        """
        playlist.export(path if path else 'playlist{0}.mp3'.format(datetime.now().strftime('%Y%m%d%H%M%S')))