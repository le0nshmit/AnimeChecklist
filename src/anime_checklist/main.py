from anime_checklist.utils import menu_validation, clear
from anime_checklist.view import list_anime
from anime_checklist.modify import modify_main
import sys

MAIN_MENU = {
    '1' : list_anime,
    '2' : lambda: modify_main(clear),
    'exit': sys.exit,
}


def main() -> None:
    clear()
    print("\n\n[> Anime Check List <]\n\n")
    while True:
        print("[> 1) View Anime List <]\n[> 2) Modify Anime List <]")
        command = input("> ")
        menu_validation(command, MAIN_MENU)

if __name__  == '__main__': main()


