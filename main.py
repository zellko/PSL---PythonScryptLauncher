import os
import subprocess
from data import Data
from art import logo


def clear_screen(print_info=""):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print("\nWelcome to Python Script Launcher")
    data.read_csv()
    print(print_info)


data = Data()
clear_screen()

quite_program = False
while not quite_program:
    info = ""

    user_input = input(f"Type 1 to {len(data.script_data['name'])} to launch corresponding application."
                       f"\nType 'add' to add new application, 'remove' to remove application, 'q' to quit ")

    if user_input.lower() == "q":
        quite_program = True
    elif user_input.lower() == "add":
        info = data.add_to_csv()
    elif user_input.lower() == "remove":
        data.remove_to_csv()
    elif not user_input.isnumeric():
        info = "\n--> Invalid command\n"
    elif int(user_input) <= len(data.script_data["name"]) and len(data.script_data["name"]) > 0:
        if data.script_data.columns[3] == "gnome":
            os.system(f'gnome-terminal [-e], -- {data.script_data["path"][int(user_input) - 1]}')
        else:
            # TODO Figure out why xterm is closed when python is closed but not gnome
            os.system(f'xterm -e {data.script_data["path"][int(user_input) - 1]}')
    else:
        info = "\n--> Invalid command\n"

    clear_screen(print_info=info)

# TODO Clean Up
# TODO Add comments
# TODO Simplify removing process?
