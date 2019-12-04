# Imports and constants
import sys
import shutil
from msvcrt import getch
import os
import IL_Constants

# Classes
class IL_MainMenu():
    ''' '''

    FILE = 'InterfaceLayer/UI_MetaData/MainMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/MainMenu_graphics.txt'
    ADDRESS = 'Main Menu'
    PARENT = 'IL_MainMenu'
    YOU_ARE_HERE = 'IL_MainMenu'
    QUITSCREEN = 'InterfaceLayer/UI_MetaData/QuitScreen.txt'
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
            if IL_Constants.SEPERATOR in line:
                self.print_seperator()
            elif IL_Constants.GRAPHICS in line:
                self.print_file(graphics)
            elif IL_Constants.CENTER_JUST in line:
                self.print_centerJust(line)
            elif IL_Constants.RIGHT_JUST in line:
                if IL_Constants.INDENT in line:
                    self.print_rightJust_indent(line)
                else:
                    self.print_rightJust(line)
            elif IL_Constants.LEFT_JUST in line:
                if IL_Constants.INDENT in line:
                    self.print_leftJust_indent(line)
                else:
                    self.print_leftJust(line)
            elif IL_Constants.SPACING in line:
                self.print_spaceing(file, graphics)
            elif IL_Constants.EMPTY_LINE in line:
                self.print_emptyline()
            elif IL_Constants.BREAD_CRUMBS in line:
                self.print_breadcrumbs(self.ADDRESS)
                
    def print_spaceing(self, file = '', graphics = ''):
        counter = 3
        for line in self.get_file(file):
            if IL_Constants.GRAPHICS in line:
                for line in self.get_file(graphics):
                    counter += 1
            else:
                counter += 1
        for _ in range(self.__window_height - counter):
            print((IL_Constants.SPACE * 4) + IL_Constants.VERTICAL + (IL_Constants.SPACE * (self.__window_width - 10)) + IL_Constants.VERTICAL)
            
    def print_centerJust(self, line):
        print((IL_Constants.SPACE * 4) + IL_Constants.VERTICAL + line.replace(IL_Constants.CENTER_JUST, '').center(self.__window_width - 10) + IL_Constants.VERTICAL)

    def print_rightJust_indent(self, line):
        print((IL_Constants.SPACE * 4) + IL_Constants.VERTICAL + line.replace(IL_Constants.RIGHT_JUST+IL_Constants.INDENT, '').rjust(self.__window_width -15) + (IL_Constants.SPACE * 5) + IL_Constants.VERTICAL)
    
    def print_rightJust(self, line):
        print((IL_Constants.SPACE * 4) + IL_Constants.VERTICAL + line.replace(IL_Constants.RIGHT_JUST, '').rjust(self.__window_width -10) + IL_Constants.VERTICAL)

    def print_leftJust_indent(self, line):
        print((IL_Constants.SPACE * 4) + IL_Constants.VERTICAL + (IL_Constants.SPACE * 5) + line.replace(IL_Constants.LEFT_JUST+IL_Constants.INDENT, '').ljust(self.__window_width -15) + IL_Constants.VERTICAL)
    
    def print_leftJust(self, line):
        print((IL_Constants.SPACE * 4) + IL_Constants.VERTICAL + line.replace(IL_Constants.LEFT_JUST, '').ljust(self.__window_width -10) + IL_Constants.VERTICAL)
    
    def print_seperator(self):
        print((IL_Constants.SPACE * 4) + IL_Constants.CROSS + (IL_Constants.HORIZONTAL * (self.__window_width - 10)) + IL_Constants.CROSS)

    def print_file(self, file):
        for line in self.get_file(file):
            print((IL_Constants.SPACE * 4) + IL_Constants.CROSS + line.center(self.__window_width - 10, IL_Constants.HORIZONTAL) + IL_Constants.CROSS)
    
    def print_emptyline(self):
        print((IL_Constants.SPACE * 4) + IL_Constants.VERTICAL + (IL_Constants.SPACE * (self.__window_width - 10)) + IL_Constants.VERTICAL)
    
    def print_breadcrumbs(self, address):
        print((IL_Constants.SPACE * 4) + IL_Constants.VERTICAL + (IL_Constants.SPACE * 5) + address + (IL_Constants.SPACE *(self.__window_width-len(address)-15))+IL_Constants.VERTICAL)
    
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
                for key, value in IL_Constants.MENUS.items():
                    if output == key:
                        output = value
        return (_input, output)        

    def validate_selection(self):        
        print('Enter your selction:')
        user_input = self.select_fromMenu()
        if user_input == 'q':
            return 'q'
        elif user_input:
            return user_input
        else:
            return False 
    
    def quitscreen(self):
        self.print_window(self.QUITSCREEN)        