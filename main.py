import click

from aok.audio_merge import AudioMerge

@click.group()
@click.version_option()
def aok():
    """A utility to split and/or join audio files.
    """

@aok.command()
@click.option('-o', '--output', help='Output file with absolute or relative path',
                type=click.Path(), nargs=1, required=False)
@click.argument('input', type=click.File('rb'), nargs=-1, required=True)
def join(output, input):
    """Merge two or more audio files.
    """
    merger = AudioMerge(input)
    merger.merge()
    merger.export(output)
