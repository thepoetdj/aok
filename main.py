import click

@click.group()
@click.version_option()
def aok():
    """A utility to split and/or join audio files.
    """

@aok.command()
@click.option('-o', '--output', help='Output file with absolute or relative path',
                type=click.Path(exists=True), nargs=1, required=False)
@click.argument('input', type=click.File(), nargs=-1, required=True)
def join(output, input):
    """Merge two or more audio files.
    """
    for audio_file in input:
        # merge audio files to specified output file
        pass
