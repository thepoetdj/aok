# aok

`aok` is a command-line utility to split an audio file or join multiple audio files into one or do both.

## Dependencies

[pydub](https://github.com/jiaaro/pydub), for audio processing

[Click](https://click.palletsprojects.com/en/7.x/), for the command-line interface

## Installation

**Note:** We use and recommend [pipenv](https://github.com/pypa/pipenv) to install and manage `aok` and its dependencies.

Let's clone this repository and change into it:

```
$ git clone https://github.com/DhruvPJoshi/aok.git && cd aok
```

Ensure that `pipenv` is installed and then create a virtual environment into the changed directory:

```
$ pipenv shell
```

Once the virtual environment is created and activated, install `aok`:

```
$ pipenv install -e .
```

## Usage

Once installed, checkout the basic help message:

```
$ aok --help

Usage: aok [OPTIONS] COMMAND [ARGS]...

  A utility to split and/or join audio files.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  join  Merge two or more audio files.
```

**Note:** As `aok` is in active development, more commands will be added soon.

### Join audio files

Take a look at the help message of `join` command:

```
$ aok join --help

Usage: aok join [OPTIONS] INPUT...

  Merge two or more audio files.

Options:
  -f, --format [mp3|wav|aif|ogg]  The format of both input and output audio
  -o, --output PATH               Output file with absolute or relative path
  --help                          Show this message and exit.
```

With `aok`, you can merge multiple audio files into a single playlist. What's more, you can also specify the audio format!

Let's merge few audio files. `aok` supports `mp3` extension by default.

```
$ aok join '100degrees.mp3' 'Dirty Disco.mp3' 'LA FIESTA.mp3'
Playlist created successfully!
```

Once you get the success message, checkout your current directory for the exported playlist.

The default output file has temporary name. If you want a specific name for your playlist, then use the `-o/--output` option:

```
$ aok join --output 'My Playlist.mp3' ...
```

As mentioned earlier, you can use `aok` on different audio formats:

```
$ aok join --format wav --output repeated_explosion.wav explosion.wav
```

(*__Note__: Both the input and output audio has to be of same format for the `-f/--format` option to work.*)

Did you notice that I gave only one audio as input? In such cases, the `join` command will simply repeat the audio in exported playlist. Cool, isn't it?