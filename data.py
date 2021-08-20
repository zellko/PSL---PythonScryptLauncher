import pandas
import os
import stat
import pathlib


class Data:
    def __init__(self):
        """Check if the CSV is present, if not create on"""
        try:
            self.script_data = pandas.read_csv("cmd_path.csv")
        except FileNotFoundError:
            dataframe = pandas.DataFrame(columns=["path", "name"])
            dataframe.to_csv("cmd_path.csv")
        self.read_csv()

    def read_csv(self):
        """Read the CSV file and print the content"""
        self.script_data = pandas.read_csv("cmd_path.csv")
        for (index, row) in self.script_data.iterrows():
            print(f"{index + 1}. {row['name']}")

    def add_script_to_csv(self):
        """Add a script to the CSV file"""
        path = input("Enter script path or command: ")
        name = input("Enter the name of the application: ")

        if len(path) == 0 or len(name) == 0:
            return "\n--> You need to enter a path/command and a name !\n"
        new_row = {f"path": path, "name": name}

        self.script_data = self.script_data.append(new_row, ignore_index=True)
        self.update_csv_file()
        return ""

    def add_cmd_to_csv(self):
        """Add a command to the CSV file - but we first need convert the command into a scrip"""
        cmd = input("Enter the command: ")
        name = input("Enter the name of the application: ")

        if len(cmd) == 0 or len(name) == 0:
            return "\n--> You need to enter a path/command and a name !\n"

        # Create the script file
        with open(f"{name}.sh", "w") as script:
            script.write(f"#!/bin/bash\n{cmd}")

        # Make it executable
        st = os.stat(f"{name}.sh")
        os.chmod(f"{name}.sh", st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

        # Get the path of directory
        path = pathlib.Path().resolve()
        new_row = {f"path": f"{path}/{name}.sh", "name": name}

        # Append the script absolute path and name to the CSV
        self.script_data = self.script_data.append(new_row, ignore_index=True)
        self.update_csv_file()
        return ""

    def remove_to_csv(self):
        """Remove a command to the CSV file"""
        row = int(input(f"Which application would you like to remove? Type 1 to {len(self.script_data['name'])}: "))
        self.script_data = self.script_data.drop([row - 1])
        self.update_csv_file()

    def update_csv_file(self):
        """Write the CSV  with the new value"""
        self.script_data.to_csv("cmd_path.csv", header=True, index=False)
