# PSL - PythonScriptLauncher

![CLI](https://raw.githubusercontent.com/zellko/PSL-PythonScriptLauncher/main/Documentation/cli.png)

_WORK IN PROGRESS - My goal is to develop this project in parallel of my Python lessons_

My first personal project - A CLI Python Script launcher for Linux beginner.

PSL is software, targeting Linux beginner user, allowing them to quickly launch their applications/commands or scripts without the need of using the terminal.

PSL display to the user the list of scripts that he previously added, and allow him to launch them by simply selecting one of them.

Typically, PLS would be launched at the startup of the OS to be used as a kind of quick startup menu.

**If you see any improvements, errors or bad practice in the code, please feel free to comment. My goal is to improve my skills.**

## Background
On Windows, almost all the software use .exe extension and have GUI. 

Switching to Linux (PopOs) from Windows, I discovered that I will have to deal with different "kinds" of software.

1. Some are installed from package/Pop Store
2. Some .appimage
3. Some need to be started by a script, through the terminal (e.g. PyCharm).
4. Some without GUI, who need to be used by passing command through terminal (e.g. ExpressVPN)

Software from package or appimage are easy to handle. On the other hand, it's sometimes annoying to always have to use the terminal to launch a script or use a software without GUI. So I decided to create this small application in order to facilitate my life.

## Installation guide - Standalone executable
Coming soon

## Installation guide - Python3
Coming soon

## How to use it

#### Adding a script:
![AddScript](/home/zellkoss/Documents/python_programming/PSL-PythonScriptLauncher/Documentation/add_s_0.png)
1. Type AddS
2. Enter the script absolute path: e.g.: `/home/zellkoss/Programme/pycharm-community-2021.2/bin/pycharm.sh`
3. Enter the name that you would like to give to the script:  e.g.: `PyCharm Test`

Your new application is now added to you list of applications!
![AddScript](/home/zellkoss/Documents/python_programming/PSL-PythonScriptLauncher/Documentation/add_s.png)

#### Adding a command:
![AddCommand](/home/zellkoss/Documents/python_programming/PSL-PythonScriptLauncher/Documentation/add_c_0.png)
1. Type AddC
2. Enter the command: e.g.: `expressvpn connect`
3. Enter the name that you would like to give to the script:  e.g.: `VPN Connect Test`

Note: When creating a command, it will be converted to a script. The script will be created on the same folder PythonScriptLauncher

Your new application is now added to you list of applications!

#### Removing an app:
![AddCommand](/home/zellkoss/Documents/python_programming/PSL-PythonScriptLauncher/Documentation/remove_0.png)
1. Type remove
2. Enter the application number: e.g.: `6`

The application is now removed!

### Tested on:
- Pop!_OS 21.04


