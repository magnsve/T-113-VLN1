# Imports and constants
import sys
import shutil

CROSS = '+'
VERTICAL = '|'
HORIZONTAL = '-'
SPACE = ' '

# Classes
class MainMenu():
    def __init__(self):
        self.__window_width = self.get_window_size()[0]
        self.__window_height = self.get_window_size()[1]

    def __str__(self):
        return 'Window is {} columns and {} rows.'.format(self.__window_width, self.__window_height)

    def print_window(self):
        pass

    def get_window_size(self):
        return shutil.get_terminal_size()

# Functions
def main():
    start = MainMenu()
    print(start)


# Main program
main()