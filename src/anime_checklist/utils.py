from time import sleep
import os

clear = lambda: os.system('clear')

def menu_validation(command, menu): 
    if command in menu: menu[command]()
    else: 
        print("[> must be in range or 'exit' <]"), 
        sleep(1), clear()