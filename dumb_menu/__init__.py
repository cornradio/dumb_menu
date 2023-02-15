import os
import re

#region windows
def get_menu_choice1(options):
    shortcuts = scan_short_cuts(options) # scan for shortcuts
    selected_index = 0
    while True:
        os.system("cls" if os.name == "nt" else "clear") #clear screen
        show_menu(options,selected_index)

        key = b'\a' #default to error
        try:
            import msvcrt
            char = msvcrt.getch() #get keypress
        except :
            pass

        if key == b'\x1b':  # Esc key to exit
            return -1
        elif key == b'\r':  # Enter key to select
            return selected_index
        elif key in (b'\x48', b'\x50'):  # Up or Down arrow
            selected_index = (selected_index + (1 if key == b'\x50' else -1) + len(options)) % len(options)
        elif key in shortcuts: # Shortcut key
            return shortcuts[key]
        elif key == b'\a':
            print('error , may not support your system')
            exit()
# endregion
def get_key(): #get keypress using getch , msvcrt = windows or termios = linux
    try :
        import getch
        first_char = getch.getch()
        if first_char == '\x1b': #arrow keys
            a=getch.getch()
            b=getch.getch()
            return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left' }[a+b]
        if ord(first_char) == 10:
            return  'enter'
        if ord(first_char) == 32:
            return  'space'
        else:
            return first_char #normal keys like abcd 1234
    except :
        pass
    try:
        import msvcrt
        key = msvcrt.getch()  # get keypress
        if key == b'\x1b':  # Esc key to exit
            return 'esc'
        elif key == b'\r':  # Enter key to select
            return 'enter'
        elif key == b'\x48':  # Up or Down arrow
            return  'up'
        elif key == b'\x50':  # Up or Down arrow
            return 'down'
        else:
            return key.decode('utf-8')
    except:
        pass


def get_menu_choice(options):
    shortcuts = scan_short_cuts(options)  # scan for shortcuts
    selected_index = 0
    print(shortcuts)
    while True:
        show_menu(options, selected_index)
        key = get_key()
        if key == 'enter':  # Enter key to select
            return selected_index
        elif key in ('up','down'):  # Up or Down arrow
            selected_index = (selected_index + (1 if key == 'down' else -1) + len(options)) % len(options)
        elif key in shortcuts:  # Shortcut key
            return shortcuts[key]

def scan_short_cuts(options):
    shortcuts = {}
    for i, option in enumerate(options):
        match = re.match(r"\[(.*)\](.*)", option)
        if match:
            shortcut, text = match.group(1, 2)
            shortcuts[shortcut] = i
    return shortcuts


def show_menu(options, selected_index):
    os.system("cls" if os.name == "nt" else "clear")
    print("Menu","current option:",selected_index)
    for i, option in enumerate(options):
        if i == selected_index:
            print(f"> {option}")
        else:
            print(f"  {option}")
    print("\nUse the arrow keys to move, Enter/key to select.")



def demo():
    options = ["[1]Option 1", "[2]Option 2", "[3]Option 3","[q]quit"]
    index = get_menu_choice(options)

    if index != -1:
        print(f"You selected option {index + 1}: {options[index]}")
    else:
        print("You exited the menu.")
