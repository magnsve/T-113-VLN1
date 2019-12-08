# Imports and constants
import sys
import shutil
from msvcrt import getch
import os

CROSS = '+'
VERTICAL = '|'
HORIZONTAL = '-'
SPACE = ' '
SEPERATOR = '--sep--'
GRAPHICS = '--gra--'
CENTER_JUST = '--cen--'
RIGHT_JUST = '--rju--'
INDENT = '--ind--'
LEFT_JUST = '--lju--'
SPACING = '--spa--'
EMPTY_LINE = '--emp--'
BREAD_CRUMBS = '--bre--'
SECOND_INDENT = '--sec--'
OPTION1 = '--o01--'
OPTION2 = '--o02--'
OPTION3 = '--o03--'
OPTION4 = '--o04--'
OPTION5 = '--o05--'
OPTION6 = '--o06--'
OPTION7 = '--o07--'
MENUS = {'M': 'IL_MainMenu', 'M_1': 'IL_EmployeeMenu', 'M_1_1':'IL_EmployeeCreateMenu', 'M_1_2': 'IL_EmployeeSearchMenu', 'Q':'IL_QuitScreen'}

# Classes
class IL_MainMenu():
    ''' '''

    FILE = 'UI_MetaData/MainMenu.txt'
    GRAPHICS_FILE = 'UI_MetaData/MainMenu_graphics.txt'
    ADDRESS = 'Main Menu'
    PARENT = 'IL_MainMenu'
    YOU_ARE_HERE = 'IL_MainMenu'
    QUITSCREEN = 'UI_MetaData/QuitScreen.txt'
    OPTIONS = [('1','M_1'),('2','M_2'),('3','M_3'),('4','M_4'),('r','M'),('q','Q'),('b','M')]

    def __init__(self):
        self.__window_width = self.get_window_size()[0]
        self.__window_height = self.get_window_size()[1]

    def __str__(self):
        return 'Window is {} columns and {} rows.'.format(self.__window_width, self.__window_height)
    
    def variable_class(self, string = ''):
        class_ = globals()[string]
        return class_()

    def print_window(self, file = FILE, graphics = GRAPHICS_FILE):
        for _ in range(self.__window_height):  # Clear the previous screen to prevent 'bleeding'.
            print()
        main_menu = self.get_file(file)
        for line in main_menu:
            if SEPERATOR in line:
                self.print_seperator()
            elif GRAPHICS in line:
                self.print_file(graphics)
            elif CENTER_JUST in line:
                self.print_centerJust(line)
            elif RIGHT_JUST in line:
                if INDENT in line:
                    self.print_rightJust_indent(line)
                else:
                    self.print_rightJust(line)
            elif LEFT_JUST in line:
                if INDENT in line:
                    self.print_leftJust_indent(line)
                else:
                    self.print_leftJust(line)
            elif SPACING in line:
                self.print_spaceing(file, graphics)
            elif EMPTY_LINE in line:
                self.print_emptyline()
            elif BREAD_CRUMBS in line:
                self.print_breadcrumbs(self.ADDRESS)
            elif INDENT in line:
                self.print_secondIndent()
                
    def print_spaceing(self, file = '', graphics = ''):
        counter = 3
        for line in self.get_file(file):
            if GRAPHICS in line:
                for line in self.get_file(graphics):
                    counter += 1
            else:
                counter += 1
        for _ in range(self.__window_height - counter):
            print((SPACE * 4) + VERTICAL + (SPACE * (self.__window_width - 10)) + VERTICAL)
    
    def print_secondIndent(self):
        print()
            
    def print_centerJust(self, line):
        print((SPACE * 4) + VERTICAL + line.replace(CENTER_JUST, '').center(self.__window_width - 10) + VERTICAL)

    def print_rightJust_indent(self, line):
        print((SPACE * 4) + VERTICAL + line.replace(RIGHT_JUST+INDENT, '').rjust(self.__window_width -15) + (SPACE * 5) + VERTICAL)
    
    def print_rightJust(self, line):
        print((SPACE * 4) + VERTICAL + line.replace(RIGHT_JUST, '').rjust(self.__window_width -10) + VERTICAL)

    def print_leftJust_indent(self, line):
        print((SPACE * 4) + VERTICAL + (SPACE * 5) + line.replace(LEFT_JUST+INDENT, '').ljust(self.__window_width -15) + VERTICAL)
    
    def print_leftJust(self, line):
        print((SPACE * 4) + VERTICAL + line.replace(LEFT_JUST, '').ljust(self.__window_width -10) + VERTICAL)
    
    def print_seperator(self):
        print((SPACE * 4) + CROSS + (HORIZONTAL * (self.__window_width - 10)) + CROSS)

    def print_file(self, file):
        for line in self.get_file(file):
            print((SPACE * 4) + CROSS + line.center(self.__window_width - 10, HORIZONTAL) + CROSS)
    
    def print_emptyline(self):
        print((SPACE * 4) + VERTICAL + (SPACE * (self.__window_width - 10)) + VERTICAL)
    
    def print_breadcrumbs(self, address):
        print((SPACE * 4) + VERTICAL + (SPACE * 5) + address + (SPACE *(self.__window_width-len(address)-15))+VERTICAL)
    
    def get_file(self, file):
        filestream = open(file,'r')
        output = []
        output += [line.strip('\n') for line in filestream]
        filestream.close()
        return output

    def get_window_size(self):
        return shutil.get_terminal_size()
    
    def single_input(self):        
        try:
            return getch().decode('ASCII').lower()
        except UnicodeDecodeError:
            return 'z'
    
    def multi_input(self):
        return input()

    def select_fromMenu(self):                
        _input = self.single_input()                                  
        output = False
        if output == False:
            if _input == 'q':            
                return 'q'
            else:
                for item in self.OPTIONS:
                    if _input == item[0]:
                        output = item[1]
                for key, value in MENUS.items():
                    if output == key:
                        output = value
        return (_input, output)        

    def validate_selection(self):        
        print('Enter your selction:')
        user_input = self.select_fromMenu()
        while not user_input == 'q':
            print(user_input[0])    
            while not user_input[1]:
                self.print_window()
                print('Invalid selection, please try again:')
                user_input = self.select_fromMenu()
                print(user_input[0])
            return user_input
        else:
            return 'q'
    
    def quitscreen(self):
        self.print_window(self.QUITSCREEN)        

# Functions
def main():
    current_pos = IL_MainMenu()
    current_pos.print_window(current_pos.FILE,current_pos.GRAPHICS_FILE)    
    user_input = current_pos.validate_selection()        
    while user_input != 'q':
        new_pos = current_pos.variable_class(user_input[1])
        cleanup = current_pos.YOU_ARE_HERE
        del cleanup        
        new_pos.print_window(new_pos.FILE,new_pos.GRAPHICS_FILE)
        user_input = new_pos.validate_selection()
        current_pos = new_pos
    else:
        current_pos.quitscreen()
    
# Main program
main()


