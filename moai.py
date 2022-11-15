# Thirty Dollar Website (https://thirtydollar.website/) music file to moai file converter. 
#
# Usage: python moai.py <input_file> [OPTIONS]
#   [OPTIONS]:
#       -o : name of output file, will be prompted if not specified.
#
# The program reads the input file and write a .moai file to the user-specified output which can be loaded on the Thirty Dollar Website.
#
# The input file is a simple text file that specifies the properties and notes of the clip.
# The first line specifies the playback speed of the clip. (For reference, the site's default is 300).
# The next lines represent each track. Each track is a space separated list specified as follows:
#   - Name of the instrument/soundfx list written first <instrument>
#   - A space separated list of notes and their pitches or silence.
#       A note can either be:
#           - The name of a valid note in music theory (e.g. A#, A, B, etc.) followed by its pitch (e.g. C4, D5). C4 is "middle C"
#           - Or a . to indicate a "rest" or "silence" for that beat
#
#       Sharps can be specified with # and Flats can be specified with -, they both must be specified AFTER the name of the note
# 
# If there are multiple tracks, all of the notes from each track line-up in a one-to-one correspondence.
# So all tracks should have the same length (otherwise the length of the shortest track is used)
# Spaces do not count towards the length of the track, only notes (and rests) do.
#
# You can view some sample files in the samples/ folder 
#
# Anatomy of the input file:
#
# <speed (int)>
# <instrument1 (str)> <NOTE_SEQ1 (str_list)>
# <instrument2 (str)> <NOTE_SEQ2 (str_list)>
# ...
#
# 

import sys

SILENCE = '_pause'
COMBINE = '!combine'
SPEED_SET = '!speed@'
KEYS_TO_PITCH = {
    'B': 5,
    'A#': 4,
    'B-': 4,
    'A': 3,
    'G#': 2,
    'A-': 2,
    'G': 1,
    'F#': 0,
    'G-': 0,
    'F': -1,
    'E': -2,
    'D#': -3,
    'E-': -3,
    'D': -4,
    'C#': -5,
    'D-': -5,
    'C': -6,
}

def parse_note_token(token, sound):
    if token == '.':
        return SILENCE

    delim = len(token) - 1

    try:
        relative_pitch = KEYS_TO_PITCH[token[:delim]]
        octave = int(token[delim:]) - 4 

    except KeyError as e:
        print(f'Unknown note {e}. Failed to parse.', file=sys.stderr)
        quit()

    except ValueError:
        print(f'Note missing pitch \'{token}\'. Failed to parse.', file=sys.stderr)
        quit()

    pitch = relative_pitch + octave * 12
    return f"{sound}@{pitch}"

def get_input_file_name():
    it = iter(range(1, len(sys.argv)))

    for i in it:
        val = sys.argv[i]
        if val.startswith('-'):
            next(it) # Skip next value
            continue
    
        return val 

    print(f'Usage: {sys.argv[0]} <input_file> [OPTIONS]', file=sys.stderr)
    quit()

def get_output_file_name():
    try:
        loc = sys.argv.index('-o')
        assert loc < len(sys.argv) - 1, 'Must provide argument for -o'
        return sys.argv[loc + 1]

    except ValueError:
        return input('Enter output filename: ')

def main():
    input_file_name = get_input_file_name()
    output_file_name = get_output_file_name()

    speed = 300
    voices = []
    sounds = []

    with open(input_file_name, 'r') as in_file:
        # Load Speed
        speed = int(in_file.readline())

        # Load Notes
        for line in in_file:
            track = line.strip().split()
            sounds.append(track[0])
            voices.append(map(str.upper, track[1:]))

        assert len(voices) == len(sounds), f'Sounds ({len(sounds)}) and Voices ({len(voices)}) should be equal in length'

    with open(output_file_name, 'w') as out_file:
        out_file.write(f'{SPEED_SET}{speed}|')  

        for voices in zip(*voices):
            out_file.write('|')
            chord = [ parse_note_token(v, sounds[i]) for i, v in enumerate(voices) ]
            chord_str = f'|{COMBINE}|'.join(chord)
            out_file.write(chord_str) 

if __name__ == '__main__':
    main()
