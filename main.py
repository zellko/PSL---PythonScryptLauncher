import os
import subprocess
from data import Data
from art import logo


def clear_screen(print_info=""):
    """Function to 'refresh' the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
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
                       f"\nType 'addS' to add new script or 'addC' to add new command\n"
                       f"Type 'remove' to remove application, 'q' to quit ")

    if user_input.lower() == "q":
        quite_program = True
    elif user_input.lower() == "adds":
        info = data.add_script_to_csv()
    elif user_input.lower() == "addc":
        info = data.add_cmd_to_csv()
    elif user_input.lower() == "remove":
        data.remove_to_csv()
    elif not user_input.isnumeric():
        info = "\n--> Invalid command\n"
    elif int(user_input) <= len(data.script_data["name"]) and len(data.script_data["name"]) > 0:
        # If the user type a valid number, we execute the corresponding script
        try:
            command = {data.script_data['path'][int(user_input) - 1]}  # Get the script from the DataFrame
            subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # stdout and stderr are suppressed to avoid the application printing value on the terminal
        except FileNotFoundError as error:  # Error if the path is incorrect
            info = f"\nError: -->{error}<-- when trying to start your application\n"
        except OSError as error:  # Error if the script is empty or wrong
            info = f"\nError: -->{error}<-- when trying to start your application\n"
    else:
        info = "\n--> Invalid command\n"

    clear_screen(print_info=info)

# TODO Clean Up/Comments
# TODO Simplify removing process?
