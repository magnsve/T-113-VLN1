# Imports and constants
import sys, os, shutil, random
from msvcrt import getch
from importlib import import_module, invalidate_caches

# Classes
class IL_Printer():
    ''' '''
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
    FACTS = '--fact--'
    MENUS = {'M': 'IL_MainMenu', 'M_1': 'IL_EmployeeMenu', 'M_1_1':'IL_EmployeeCreateMenu', 'M_1_2': 'IL_EmployeeSearchMenu','M_2': 'IL_AirplaneMenu', 'M_2_1': 'IL_AirplaneCreateMenu', 'Q':'IL_QuitScreen'}

    def __init__(self):
        self.__window_width = self.get_window_size()[0]
        self.__window_height = self.get_window_size()[1]

    def get_class_name(self, string):
        module_name = 'InterfaceLayer.'+string
        class_name = string
        module = import_module(module_name)        
        _class = getattr(module, class_name)        
        return _class

    def get_window(self, name):
        class_name = self.get_class_name(name)
        file = class_name.FILE
        graphics = class_name.GRAPHICS_FILE
        main_menu = self.get_file(file)
        output = ''
        for _ in range(self.__window_height*3):
            output += '\n'
        for line in main_menu:
            if self.SEPERATOR in line:
                output += self.get_seperator() + '\n'                
            elif self.GRAPHICS in line:
                output += self.get_file_output(graphics)
            elif self.CENTER_JUST in line:
                output += self.get_centerJust(line) + '\n'                
            elif self.RIGHT_JUST in line:
                if self.INDENT in line:
                    output += self.get_rightJust_indent(line) + '\n'
                else:
                    output += self.get_rightJust(line) + '\n'                    
            elif self.LEFT_JUST in line:
                if self.INDENT in line:
                    output += self.get_leftJust_indent(line) + '\n'                    
                else:
                    output += self.get_leftJust(line) + '\n'                    
            elif self.SPACING in line:
                output += self.get_spaceing(file, graphics)           
            elif self.EMPTY_LINE in line:
                output += self.get_emptyline() + '\n'                
            elif self.BREAD_CRUMBS in line:
                output += self.get_breadcrumbs(class_name.ADDRESS) + '\n'                
            elif self.FACTS in line:
                output += self.get_fact(self.FACTS) + '\n'                
        return output
                
    def get_spaceing(self, file ='', grapics = ''):
        counter = 3
        output = ''
        for line in self.get_file(file):
            if self.GRAPHICS in line:
                for line in self.get_file(grapics):
                    counter += 1
            else:
                counter += 1
        for _ in range(self.__window_height - counter):
            left_border = (self.SPACE * 4) + self.VERTICAL
            content = self.SPACE * (self.__window_width - 10)
            right_border = self.VERTICAL
            output += '{}{}{}'.format(left_border, content, right_border) + '\n'
        return output

    def get_file_output(self, file):
        output = ''
        for line in self.get_file(file):
            left_border = (self.SPACE * 4) + self.CROSS
            content = line.center(self.__window_width -10, self.HORIZONTAL)
            right_border = self.CROSS
            output += '{}{}{}'.format(left_border,content,right_border) + '\n'
        return output
        
    def get_fact(self, facts):
        _facts = self.get_file(facts)
        fact = _facts[random.randint(0,len(_facts)+1)]
        left_border = (self.SPACE * 4) + self.VERTICAL
        content = ('...'+fact).rjust(self.__window_width-15)
        right_border = (self.SPACE * 5) + self.VERTICAL
        return '{}{}{}'.format(left_border, content, right_border)    
            
    def get_centerJust(self, line):
        left_border = (self.SPACE * 4) + self.VERTICAL
        content = line.replace(self.CENTER_JUST, '').center(self.__window_width - 10)
        right_border = self.VERTICAL
        return '{}{}{}'.format(left_border, content, right_border)

    def get_rightJust_indent(self, line):
        left_border = (self.SPACE * 4) + self.VERTICAL
        content = line.replace(self.RIGHT_JUST+self.INDENT, '').rjust(self.__window_width -15) + (self.SPACE * 5)
        right_border = self.VERTICAL
        return '{}{}{}'.format(left_border, content, right_border)

    def get_rightJust(self, line):
        left_border = (self.SPACE * 4) + self.VERTICAL
        content = line.replace(self.RIGHT_JUST, '').rjust(self.__window_width -10)
        right_border = self.VERTICAL
        return '{}{}{}'.format(left_border, content, right_border)

    def get_leftJust_indent(self, line):
        left_border = (self.SPACE * 4) + self.VERTICAL + (self.SPACE * 5)
        content = line.replace(self.LEFT_JUST+self.INDENT, '').ljust(self.__window_width -15)
        right_border = self.VERTICAL
        return '{}{}{}'.format(left_border, content, right_border)

    def get_leftJust(self, line):
        left_border = (self.SPACE * 4) + self.VERTICAL
        content = line.replace(self.LEFT_JUST, '').ljust(self.__window_width -10)
        right_border = self.VERTICAL
        return '{}{}{}'.format(left_border, content, right_border)    
    
    def get_seperator(self):
        left_border = (self.SPACE * 4) + self.CROSS
        content = self.HORIZONTAL * (self.__window_width - 10)
        right_border = self.CROSS
        return '{}{}{}'.format(left_border, content, right_border)

    def get_emptyline(self):
        left_border = (self.SPACE * 4) + self.VERTICAL
        content = self.SPACE * (self.__window_width - 10)
        right_border = self.VERTICAL
        return '{}{}{}'.format(left_border, content, right_border)

    def get_breadcrumbs(self, address):
        left_border = (self.SPACE * 4) + self.VERTICAL + (self.SPACE * 5)
        content = address + (self.SPACE * (self.__window_width-len(address)-15))
        right_border = self.VERTICAL
        return '{}{}{}'.format(left_border, content, right_border)    
    
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

    def select_fromMenu(self, _class):
        _input = self.single_input()                                  
        output = False                
        for item in _class.OPTIONS:
            if _input == item[0]:
                output = item[1]
        for key, value in self.MENUS.items():
            if output == key:
                output = value        
        return (_input, output)        

    def validate_selection(self, string=''):
        print('Enter your selction:')
        _class = self.get_class_name(string)
        user_input = self.select_fromMenu(_class)
        while not user_input[1]:
            print(self.get_window(_class))
            print('Invalid selection, please try again:')
            user_input = self.select_fromMenu(_class)
        return user_input