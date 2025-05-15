# Thirty Dollar Website (https://thirtydollar.website/) music file to moai file converter. 

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

def parse_note_token(token, sound, transpose = 0):
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

    pitch = relative_pitch + octave * 12 + transpose
    return f'{sound}@{pitch}'

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
    transpose = []

    with open(input_file_name, 'r') as in_file:
        # Load Speed
        speed = int(in_file.readline())

        # Load Notes
        for line in in_file:
            track = line.strip().split()
            sound = track[0].split('+')
            sounds.append(sound[0])
            transpose.append(int(sound[1]) if len(sound) > 1 else 0)
            voices.append(map(str.upper, track[1:]))

        assert len(voices) == len(sounds), f'Sounds ({len(sounds)}) and Voices ({len(voices)}) should be equal in length'

    with open(output_file_name, 'w') as out_file:
        out_file.write(f'{SPEED_SET}{speed}|')  

        for voices in zip(*voices):
            out_file.write('|')
            chord = [ parse_note_token(v, sounds[i], transpose[i]) for i, v in enumerate(voices) ]

            # Optimization
            chord = list(filter(lambda n: n != SILENCE, chord))

            if len(chord) > 0:
                chord_str = f'|{COMBINE}|'.join(chord)
            else:
                chord_str = SILENCE

            out_file.write(chord_str) 

if __name__ == '__main__':
    main()
