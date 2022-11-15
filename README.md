# [Thirty Dollar Website](https://thirtydollar.website/) music file to moai file converter

## Usage

Usage: `python moai.py <input_file> [OPTIONS]`
 - [OPTIONS]:

    `-o` : name of output file, will be prompted if not specified.

The program reads the input file and write a `.moai` file to the user-specified output which can be loaded on the [Thirty Dollar Website](https://thirtydollar.website/).

## Input Files

The input file is a simple text file that specifies the properties and notes of the clip.
The first line specifies the playback speed of the clip. (For reference, the site's default is 300).
The next lines represent each track. Each track is a space separated list specified as follows:
  - Name of the instrument/soundfx list written first `<instrument>`
  - A space separated list of notes and their pitches or silence. 
  - A note can either be:
    - The name of a valid note in music theory (e.g. `A`, `A#`, `B`, etc.) followed by its pitch (e.g. `C4`, `D5`). `C4` is "middle C"
    - Or a `.` to indicate a "rest" or "silence" for that beat
        - Sharps can be specified with `#` and Flats can be specified with `-`, they both must be specified **after** the name of the note (e.g. `A#4`, `B-4`)

If there are multiple tracks, all of the notes from each track line-up in a one-to-one correspondence.
So all tracks should have the same length (otherwise the length of the shortest track is used)
Spaces do not count towards the length of the track, only notes (and rests) do.

You can view some sample files in the `samples/` folder 

Anatomy of the input file:

```
<speed (int)>
<instrument1 (str)> <NOTE_SEQ1 (str_list)>
<instrument2 (str)> <NOTE_SEQ2 (str_list)>
...
```

## The Y

Y this exist? Y when I do this when I can just use the site? 


<p align="center">
  <img src="https://user-images.githubusercontent.com/33503562/202020526-41430387-da08-4506-8a57-1c1b36476271.gif" style="height:500px;" />
  <img src="https://user-images.githubusercontent.com/33503562/202020633-665a070a-e4c3-4cc8-8134-d186093d7d29.gif" />
</p>


WELL because I want to do **polyphonic music** ok??? and polyphonic music very very not easy on the site ***understand????***

