import click

@click.command()
@click.version_option()
def aok():
    """A utility to split and/or join audio files.
    """
    click.echo("hello world")