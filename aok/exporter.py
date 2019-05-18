from datetime import datetime

class Exporter:
    @staticmethod
    def export(path, playlist):
        """Exports playlist to the path specified.

        If no path is present, a temporary file is generated in current directory.
        """
        playlist.export(path if path else 'playlist{0}.mp3'.format(datetime.now().strftime('%Y%m%d%H%M%S')))