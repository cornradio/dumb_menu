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

if __name__ == "__main__":
    while True:
        loopmenu()