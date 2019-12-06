# Imports and constants
import sys, os, shutil, random
from msvcrt import getch
from .il_constants import IL_Constants
from importlib import import_module, invalidate_caches

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
    
    def variable_class(self, string = ''):
        module_name = 'InterfaceLayer.'+string
        class_name = string
        module = import_module(module_name)
        class_ = getattr(module, class_name)        
        return class_()
    
    def prep_window(self, file = FILE, graphics = GRAPHICS_FILE):
        output = ''
        for _ in range(self.__window_height*3):
            output += '\n'
        main_menu = self.get_file(file)
        for line in main_menu:
            if IL_Constants.SEPERATOR in line:
                output += self.get_seperator() + '\n'
            elif IL_Constants.GRAPHICS in line:
                output += self.get_file_contents(graphics)
            elif IL_Constants.CENTER_JUST in line:
                output += self.get_centerJust(line) + '\n'
            elif IL_Constants.RIGHT_JUST in line:
                if IL_Constants.INDENT in line:
                    output += self.get_rightJust_indent(line) + '\n'
                else:
                    output += self.get_rightJust(line) + '\n'
            elif IL_Constants.LEFT_JUST in line:
                if IL_Constants.INDENT in line:
                    output += self.get_leftJust_indent(line) + '\n'
                else:
                    output += self.get_leftJust(line) +'\n'
            elif IL_Constants.SPACING in line:
                output += self.get_spaceing(file, graphics)
            elif IL_Constants.EMPTY_LINE in line:
                output += self.get_emptyline() + '\n'
            elif IL_Constants.BREAD_CRUMBS in line:
                output += self.get_breadcrumbs(self.ADDRESS) + '\n'
            elif IL_Constants.FACTS in line:
                output += self.get_fact(self.FACTS) + '\n'
        return output
                
    def get_spaceing(self, file = '', graphics = ''):
        counter = 3
        output = ''
        for line in self.get_file(file):
            if IL_Constants.GRAPHICS in line:
                for line in self.get_file(graphics):
                    counter += 1
            else:
                counter += 1
        for i in range(self.__window_height - counter):
            left_border = (IL_Constants.SPACE * 4) + IL_Constants.VERTICAL
            contents = IL_Constants.SPACE * (self.__window_width - 10)
            right_border = IL_Constants.VERTICAL
            output += '{}{}{}'.format(left_border, contents, right_border) + '\n'
        return output

    def get_file_contents(self, file):
        output = ''
        for line in self.get_file(file):
            left_border = (IL_Constants.SPACE * 4) + IL_Constants.CROSS
            contents = line.center(self.__window_width - 10, IL_Constants.HORIZONTAL)
            right_border = IL_Constants.CROSS
            output += '{}{}{}'.format(left_border, contents, right_border) + '\n'
        return output
        
    def get_fact(self, facts):        
        _facts = self.get_file(facts)
        fact = _facts[random.randint(0,len(_facts))]
        left_border = (IL_Constants.SPACE * 4) + IL_Constants.VERTICAL
        contents = ('...'+fact).rjust(self.__window_width-15) + (IL_Constants.SPACE * 5)
        right_border = IL_Constants.VERTICAL
        return '{}{}{}'.format(left_border, contents, right_border)
            
    def get_centerJust(self, line):
        left_border = (IL_Constants.SPACE * 4) + IL_Constants.VERTICAL
        contents = line.replace(IL_Constants.CENTER_JUST, '').center(self.__window_width - 10)
        right_border = IL_Constants.VERTICAL
        return '{}{}{}'.format(left_border, contents, right_border)

    def get_rightJust_indent(self, line):
        left_border = (IL_Constants.SPACE * 4) + IL_Constants.VERTICAL
        contents = line.replace(IL_Constants.RIGHT_JUST+IL_Constants.INDENT, '').rjust(self.__window_width -15) + (IL_Constants.SPACE * 5)
        right_border = IL_Constants.VERTICAL
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_rightJust(self, line):
        left_border = (IL_Constants.SPACE * 4) + IL_Constants.VERTICAL
        contents = line.replace(IL_Constants.RIGHT_JUST, '').rjust(self.__window_width -10)
        right_border = IL_Constants.VERTICAL
        return '{}{}{}'.format(left_border, contents, right_border)

    def get_leftJust_indent(self, line):
        left_border = (IL_Constants.SPACE * 4) + IL_Constants.VERTICAL
        contents = (IL_Constants.SPACE * 5) + line.replace(IL_Constants.LEFT_JUST+IL_Constants.INDENT, '').ljust(self.__window_width -15)
        right_border = IL_Constants.VERTICAL
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_leftJust(self, line):
        left_border = (IL_Constants.SPACE * 4) + IL_Constants.VERTICAL
        contents = line.replace(IL_Constants.LEFT_JUST, '').ljust(self.__window_width -10)
        right_border = IL_Constants.VERTICAL
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_seperator(self):
        left_border = (IL_Constants.SPACE * 4) + IL_Constants.CROSS
        contents = (IL_Constants.HORIZONTAL * (self.__window_width - 10))
        right_border = IL_Constants.CROSS
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_emptyline(self):
        left_border = (IL_Constants.SPACE * 4) + IL_Constants.VERTICAL
        contents = (IL_Constants.SPACE * (self.__window_width - 10))
        right_border = IL_Constants.VERTICAL
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_breadcrumbs(self, address):
        left_border = (IL_Constants.SPACE * 4) + IL_Constants.VERTICAL
        contents = (IL_Constants.SPACE * 5) + address + (IL_Constants.SPACE *(self.__window_width-len(address)-15))
        right_border = IL_Constants.VERTICAL
        return '{}{}{}'.format(left_border, contents, right_border)
    
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
        for item in self.OPTIONS:
            if _input == item[0]:
                output = item[1]
        for key, value in IL_Constants.MENUS.items():
            if output == key:
                output = value        
        return (_input, output)        

    def validate_selection(self, class_name):
        print('Enter your selction:')
        user_input = self.select_fromMenu()                
        while not user_input[1]:
            print(self.prep_window(class_name.FILE, class_name.GRAPHICS_FILE))
            print('Invalid selection, please try again:')
            user_input = self.select_fromMenu()        
        return user_input