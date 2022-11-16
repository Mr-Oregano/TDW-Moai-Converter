# Thirty Dollar Website (https://thirtydollar.website/) music file to moai file converter. 

import sys, time, os

# playsound
try:
    import playsound
    PS = True
except:
    print("[CRINGE WARNING]: IN ORDER TO USE SOME OF THE BRUH SHELL FUNCTIONALITY\n\t\t  PLAYSOUND PACKAGE MUST BE INSTALLED. THESE FEATURES\n\t\t  WILL BE DISABLED *CRINGE*")
    ps_dough = True if input("\t\t  Do you want BRUH SHELL to install play sound??? (y/n): ").strip().lower() == 'y' else False
    if ps_dough:
        PS = True
        os.system("pip3 install playsound==1.2.2")
        import playsound
        ops = os.name
        if ops == "nt":
            os.system("cls")
        elif ops == "posix":
            os.system("clear")
    else:
        PS = False

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
SHELL_COMMANDS = {
    'help': {"args": [""], "help-info": [""], "argc": 1},
    'exit': {"args": [""], "help-info": [""], "argc": 1},
    'view.samples': {"args": [""], "help-info": [""], "argc": 1},
    "minion": {"args": [""], "help-info": [""], "argc": 1},
    'bruh': {"args": ["", "-n"], "help-info": ["", "-n <number>"], "argc": 2},
    'what.da.hell': {"args": [""], "help-info": [""], "argc": 1},
    'what.da.dog.doin': {"args": [""], "help-info": [""], "argc": 1},
    'dr.spice.cranberry': {"args": [""], "help-info": [""], "argc": 1}
}
if not PS:
    SHELL_COMMANDS.pop("what.da.hell")
    SHELL_COMMANDS.pop("what.da.dog.doin")
BASE_TAG = "BRUH >>> "
WELCOME = ">>> WELCOME TO BRUH SHELL <<<\n\nRUN \"help\" TO SEE WHAT COMMANDS BRUH SHELL SUPPORT\n"

def get_sounds():
    with open('sounds/sounds.txt', 'r', encoding='utf8') as sounds:
        return '|'.join(sounds.readlines()).split('|')

def parse_note_token(token, sound):
    if token == '.':
        return SILENCE


    elif token == 'H':
        octave = 0
        relative_pitch = 0
    else:
        delim = len(token) - 1
        try:
            relative_pitch = KEYS_TO_PITCH[token[:delim]]
            octave = int(token[delim:]) - 4 

        except KeyError as e:
            print(f'Unknown note {e}. Failed to parse.', file=sys.stderr)
            return -1

        except ValueError:
            print(f'Note missing pitch \'{token}\'. Failed to parse.', file=sys.stderr)
            return -1

    pitch = relative_pitch + octave * 12
    return f"{sound}@{pitch}"

def bruh():
    print("⡏⠉⠉⠉⠉⠉⠉⠋⠉⠉⠉⠉⠉⠉⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠉⠉⠉⠹\n⡇⢸⣿⡟⠛⢿⣷⠀⢸⣿⡟⠛⢿⣷⡄⢸⣿⡇⠀⢸⣿⡇⢸⣿⡇⠀⢸⣿⡇⠀\n⡇⢸⣿⣧⣤⣾⠿⠀⢸⣿⣇⣀⣸⡿⠃⢸⣿⡇⠀⢸⣿⡇⢸⣿⣇⣀⣸⣿⡇⠀\n⡇⢸⣿⡏⠉⢹⣿⡆⢸⣿⡟⠛⢻⣷⡄⢸⣿⡇⠀⢸⣿⡇⢸⣿⡏⠉⢹⣿⡇⠀\n⡇⢸⣿⣧⣤⣼⡿⠃⢸⣿⡇⠀⢸⣿⡇⠸⣿⣧⣤⣼⡿⠁⢸⣿⡇⠀⢸⣿⡇⠀\n⣇⣀⣀⣀⣀⣀⣀⣄⣀⣀⣀⣀⣀⣀⣀⣠⣀⡈⠉⣁⣀⣄⣀⣀⣀⣠⣀⣀⣀⣰")

def tokenize_command(command):
    tokens = command.split(' ')
    if len(tokens) == 1:
        return tokens[0], None, None
    elif len(tokens) == 2:
        return tokens[0], tokens[1], None
    elif len(tokens) == 3:
        return tokens[0], tokens[1], tokens[2]
    else:
        print(f"{BASE_TAG}[CRINGE ERROR]: too many arguments man. \n\t Literally follow this usage: \"command <option> <option value>\"\n\t You'll be based, thank me later")
        return "skip", None, None

def process_command(cmd, arg, arg_val):
    if   cmd == "help":
        print(f"{BASE_TAG}based BRUH SHELL commands")
        for command in SHELL_COMMANDS:
            if SHELL_COMMANDS[command]["argc"] > 1:
                for i, hlp in enumerate(SHELL_COMMANDS[command]["help-info"]):
                    if hlp != "":
                        if i == 0:
                            print(f"\t {command} {hlp} | ",end="")
                        elif i == SHELL_COMMANDS[command]["argc"] -1:
                            print(f"{command} {hlp}",end="")
                        else:
                            print(f"{command} {hlp} | ",end="")
                    else:
                        if i == 0:
                            print(f"\t {command} | ",end="")
                        elif i == SHELL_COMMANDS[command]["argc"] -1:
                            print(f"{command}",end="")
                        else:
                            print(f"{command} | ",end="")
            else:
                print(f"\t {command}", end="")
            print()
    elif cmd == "bruh":
        if arg:
            if arg_val:
                try:
                    arg_val = int(arg_val)
                    for _ in range(arg_val):
                        bruh()
                except:
                    print(f"{BASE_TAG}[CRINGE ERROR]: something ain't fly my guy, try again")
            else:
               print(f"{BASE_TAG}[CRING ERROR]: something ain't fly my guy, try again")
        else:
            bruh()
    elif cmd == "exit":
        print(f"         honestly, w move to leave this shell\n\t you will be missed bro, r.i.p")
        exit()
    elif cmd == "view.samples":
        samples = os.listdir("samples")
        for sample in  samples:
            print(f"         {sample}")
    elif cmd == "minion":
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⡿⠟⣛⣓⣲⣭⡳⣄⣀⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⢋⣴⣿⡆⠀⠀⠉⡇⢹⣟⣿⣯⣭⣉⡛⢶⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⢸⣟⠘⠉⠀⠀⢀⡼⢁⢞⣽⣯⣍⠉⠉⠙⡆⢻⡌⠙⢿⣷⣄⠀⠀⠀⠀⠀\n⣠⡤⢄⡀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣜⠻⠷⠦⠤⠖⢋⠀⣿⣿⡿⠿⠃⠀⠀⢠⠇⡾⢷⠀⠀⠙⢿⣷⣄⠀⠀⠀\n⢿⣄⡀⠙⠋⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣟⠒⠒⠒⠉⣉⣧⠙⣿⣦⣀⡀⣀⡴⣫⡾⠁⣸⣧⠀⠀⠀⢻⡇⠀⠀⠀\n ⣾⠉⣄⠀⠈⠓⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠈⠉⠀⠉⠉⠁⠈⢻⣦⣬⣭⣭⠵⠞⠋⠀⣰⣷⣿⣦⡀⠀⠀⢻⡄⠀⠀\n⠀⠈⠓⠉⠳⣄⡴⠛⢦⣀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⣤⣄⣠⡤⠚⠛⢿⣿⣿⣷⡄⠀⢸⡇⠀⠀\n⠀⠀⠀⠀⠀⠈⠹⣆⠀⠙⠷⣄⡀⠀⢠⡞⠁⢀⡴⠒⣒⠒⠲⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣆⢰⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠈⠳⢦⣀⠀⠉⣷⠋⠀⠀⣸⡀⢄⣘⣄⡀⠘⠀⠈⢙⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⠇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡾⡇⠀⠀⠀⢻⣅⣸⠀⠀⠈⠉⠳⠤⢄⡀⠈⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⡇⠀⠀⠀⠘⢿⡿⠦⣤⡤⠤⣀⠀⠀⣩⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢱⡀⠀⠀⠀⠀⠙⠒⠚⠀⠀⠚⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⢷⣾⠗⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠤⢤⣾⠁⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢇⡾⠋⠀⠀⠉⠓⠦⣤⣀⣀⡀⠀⠀⠀⠀⠀⢀⣀⠤⠖⠚⠉⣀⣠⣤⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⡞⠒⠤⢄⣀⡀⠉⠉⢹⣿⣿⠒⠋⢉⣀⡤⠴⠒⠋⠁⠀⠀⠺⣄⡀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢿⠃⠀⠀⣰⠁⠀⠀⠀⠀⡇⠀⠀⠸⠿⢿⡗⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⡜⠀⠀⠀⠘⣄⠀⠀⠀⢠⠇⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⣼⠭⠙⠛⠷⠶⣯⡀⣼⠂⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⠁⠀⠀⠀⠀⠈⠉⠒⠒⠉⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢸⡁⢀⣠⠄⠀⠀⠀⣹⠁⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠒⠒⠒⠒⠶⠶⠖⠛⣏⢀⣤⣀⠤⠞⠉⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢠⡞⠓⢄⣀⠴⠋⠉⠙⠛⠒⠒⣶⠶⠤⠤⢄⣀⡒⠒⠦⠤⠤⠤⢬⣤⠴⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠹⣦⡀⠉⠓⢦⣀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠈⠑⣄⠀⢀⣀⢀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠢⢤⣈⢓⡖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠉⠁⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠋⠉⠉⠀⠀⠀⠀⠸⣿⠿⠙⠧⠗⠈⠀⠀⠀⠀⠂")
    elif cmd == "what.da.hell":
        try:
            playsound.playsound("sounds/whatdahell.mp3")
        except:
            print("\t [CRINGE NOT BASED ERROR]: what.da.hell encountered a non-griddy error :(")
    elif cmd == "what.da.dog.doin":
        try:
            playsound.playsound("sounds/whatdadogdoin.mp3")
        except:
            print("\t [CRINGE NOT BASED ERROR]: what.da.dog.doin encountered a non-griddy error :(")
    elif cmd == "dr.spice.cranberry":
        drspicecranberry()

def shell_bosser():
    print(WELCOME)
    while True:
        command, argument, arguement_value = tokenize_command(input(BASE_TAG))
        while command not in list(SHELL_COMMANDS.keys()):
            if command != "skip": print(f"{BASE_TAG}not a valid command bro, smh")
            command, argument, arguement_value = tokenize_command(input(BASE_TAG))
        process_command(command, argument, arguement_value)

def drspicecranberry():

    snds = get_sounds()

    speed = 300
    voices = []
    sounds = []

    input_file_path = "samples/" + input("\t enter a input file for parsing (from samples): ")
    while not os.path.exists(input_file_path):
        input_file_path = "samples/" + input("\t [CRINGE ERROR]: enter a VALID input file for parsing (from samples): ")
    output_file_path = "results/parsed_" + input_file_path[8:]
    with open(input_file_path, 'r') as in_file:
        # Load Speed
        try:
            speed = int(in_file.readline())
        except:
            print("\t [CRINGE ERROR]: no speed was given. check your input file")
            return
        # Load Notes
        for line in in_file:
            track = line.strip().split()
            if not track[0] in snds:
                print(f'\t [CRINGE ERROR]: "{track[0]}" is not a valid sound. check input file')
                return
            sounds.append(track[0])
            voices.append(map(str.upper, track[1:]))

        assert len(voices) == len(sounds), f'\t [CRINGE WARNING] sounds ({len(sounds)}) and Voices ({len(voices)}) should be equal in length'
    print("\t parsing . . .")
    with open(output_file_path, 'w') as out_file:
        out_file.write(f'{SPEED_SET}{speed}|')  

        for voices in zip(*voices):
            out_file.write('|')
            chord = []
            for i, v in enumerate(voices):
                check = parse_note_token(v, sounds[i])
                if check == -1:
                    return
                chord.append(check)
            chord_str = f'|{COMBINE}|'.join(chord)
            out_file.write(chord_str)
    print(f"\t saving file to {output_file_path}")
    print(f"\t done!")

def main():
    bruh()
    shell_bosser()

if __name__ == '__main__':
    main()
