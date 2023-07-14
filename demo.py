import os
import dumb_menu

def loopmenu():
    options = ["[1]happy",
            "[2]sad",
            "[3]give me a cookie",
            "[q]quit"]
    index = dumb_menu.get_menu_choice(options,isclean = True)
    # clear screen, cls for windows, clear for linux
    os.system('cls') 
    # Python 3.10+ only,old version could use if-else
    match index:
        case 0:
            print(":)")
        case 1:
            print(":(")
        case 2:
            print("🍪ヾ(•ω•`)o")
        case 3:
            exit()
    input('Press ENTER to continue...')
    
# in this case I tried to get the key string, not the index
def loopmenu2(): 
    options = ["[z]happy",
            "[x]sad",
            "[c]give me a cookie",
            "[q]quit"]
    index = dumb_menu.get_menu_choice(options,isclean = True,give_key_str = True)
    # clear screen, cls for windows, clear for linux
    os.system('cls') 
    # Python 3.10+ only,old version could use if-else
    match index:
        case "z":
            print(":)")
        case "x":
            print(":(")
        case "c":
            print("🍪ヾ(•ω•`)o")
        case "q":
            exit()
    input('Press ENTER to continue...')

if __name__ == "__main__":
    while True:
        loopmenu2()