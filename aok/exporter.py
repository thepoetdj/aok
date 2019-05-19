from datetime import datetime

import click
from pydub import AudioSegment

class Exporter:
    @staticmethod
    def export(path: click.Path, playlist: AudioSegment, format: str) -> None:
        """Exports playlist to the path specified.

        If no path is present, a temporary file is generated in current directory.

        Parameters
        ----------
        path
            the output file path
        playlist
            the playlist to export
        format
            the exported file's format
        """
        if len(playlist) > 0:
            # export only a non empty playlist
            out = path or 'playlist{0}.{1}'.format(
                datetime.now().strftime('%Y%m%d%H%M%S'),
                format or 'mp3')
            playlist.export(out, format=format or 'mp3')