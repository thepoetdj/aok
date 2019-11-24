from typing import Sequence

import click

from aok.audio_merge import AudioMerge
from aok.audio_split import AudioSplit
from aok.exporter import Exporter

supported_formats = ['mp3', 'wav', 'aif', 'ogg']

@click.group()
@click.version_option()
def aok() -> None:
    """A utility to split and/or join audio files.
    """

@aok.command()
@click.option('-f', '--format', required=False,
    type=click.Choice(supported_formats),
    help='The format of both input and output audio')
@click.option('-o', '--output', type=click.Path(), nargs=1,
    help='Output file with absolute or relative path', required=False)
@click.argument('input', type=click.File('rb'), nargs=-1, required=True)
def join(format: str, output: click.Path, input: Sequence[click.File]) -> None:
    """Merge two or more audio files.
    """
    Exporter.export(output,
        AudioMerge.merge_all(input, format=format),
        format=format)

@aok.command()
@click.option('-f', '--format', required=False,
    type=click.Choice(supported_formats),
    help='The format of both input and output audio')
@click.option('-s', '--seconds', type=int,
    help='The number of seconds to split the song for', required=True)
@click.option('-o', '--output', type=click.Path(), nargs=1,
    help='Output file with absolute or relative path', required=False)
@click.argument('input', type=click.File('rb'), nargs=1, required=True)
def split(format: str, seconds: int, output: click.Path, input: click.File) -> None:
    """Split a song for given number of seconds.

    The seconds are counted from the beginning of the input song.
    In case the number of seconds exceeds the input song's length,
    input song will be exported as it is.
    """
    Exporter.export(output,
        AudioSplit.split_song(input, format=format, seconds=seconds),
        format=format)
