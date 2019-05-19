from typing import Sequence

import click

from aok.audio_merge import AudioMerge
from aok.exporter import Exporter

@click.group()
@click.version_option()
def aok() -> None:
    """A utility to split and/or join audio files.
    """

@aok.command()
@click.option('-f', '--format', required=False,
    type=click.Choice(['mp3', 'wav', 'aif', 'ogg']),
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
