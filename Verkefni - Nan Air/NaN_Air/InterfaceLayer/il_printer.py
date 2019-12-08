# Imports and constants
import sys, os, shutil, random
from msvcrt import getch
from importlib import import_module, invalidate_caches

# Classes
class IL_Printer():
    ''' '''
    FILE = ''
    GRAPHICS_FILE =  ''    
    
    def __init__(self):
        self.__window_width = self.get_window_size()[0]
        self.__window_height = self.get_window_size()[1]
        self.__cross = '+'
        self.__vertical = '|'    
        self.__horizontal = '-'
        self.__space =' '
        self.__seperator = '--sep--'
        self.__graphics = '--gra--'
        self.__center_just = '--cen--'
        self.__right_just = '--rju--'
        self.__indent = '--ind--'
        self.__left_just = '--lju--'
        self.__spacing = '--spa--'
        self.__empty_line = '--emp--'
        self.__bread_crumbs = '--bre--'
        self.__second_indent = '--sec--'
        self.__facts = '--fact--'
        self.__create = '--cre--'
        self.__search = '--sea--'
        self.__info = '--inf--'
        self.__menus = {'M':        ('il_main_menu',                'IL_MainMenu'),             \
                        'M_1':      ('il_employee_menu',            'IL_EmployeeMenu'),         \
                        'M_1_1':    ('il_employee_create_menu',     'IL_EmployeeCreateMenu'),   \
                        'M_1_2':    ('il_employee_search_menu',     'IL_EmployeeSearchMenu'),   \
                        'M_2':      ('il_airplane_menu',            'IL_AirplaneMenu'),         \
                        'M_2_1':    ('il_airplane_create_menu',     'IL_AirplaneCreateMenu'),   \
                        'M_2_2':    ('il_airplane_search_menu',     'IL_AirplaneSearchMenu'),   \
                        'M_3':      ('il_destination_menu',         'IL_DestinationMenu'),      \
                        'M_3_1':    ('il_destination_create_menu',  'IL_DestinationCreateMenu'),\
                        'M_3_2':    ('il_destination_search_menu',  'IL_DestinationSearchMenu'),\
                        'M_4':      ('il_trips_menu',               'IL_TripsMenu'),            \
                        'M_4_1':    ('il_trips_create_menu',        'IL_TripsCreateMenu'),      \
                        'M_4_2':    ('il_trips_search_menu',        'IL_TripsSearchMenu'),      \
                        'Q':        ('il_quit_screen',              'IL_QuitScreen')}
    
    def variable_class(self, from_menu = ('','')):
        module_name = 'InterfaceLayer.'+ from_menu[0]
        class_name = from_menu[1]
        module = import_module(module_name)
        class_ = getattr(module, class_name)        
        return class_()
    
    def prep_window(self, file = FILE, graphics = GRAPHICS_FILE, model_object = None, list_of_objects = None):
        output = ''
        for _ in range(self.__window_height*3):
            output += '\n'
        main_menu = self.get_file(file)
        for line in main_menu:
            if self.__seperator in line:
                output += self.get_seperator() + '\n'
            elif self.__graphics in line:
                output += self.get_file_contents(graphics)
            elif self.__center_just in line:
                output += self.get_centerJust(line) + '\n'
            elif self.__right_just in line:
                if self.__indent in line:
                    output += self.get_rightJust_indent(line) + '\n'
                else:
                    output += self.get_rightJust(line) + '\n'
            elif self.__left_just in line:
                if self.__indent in line:
                    output += self.get_leftJust_indent(line) + '\n'
                else:
                    output += self.get_leftJust(line) +'\n'
            elif self.__spacing in line:
                output += self.get_spaceing(file, graphics, model_object, list_of_objects)
            elif self.__empty_line in line:
                output += self.get_emptyline() + '\n'
            elif self.__bread_crumbs in line:
                output += self.get_breadcrumbs(self.ADDRESS) + '\n'
            elif self.__facts in line:
                output += self.get_fact(self.FACTS) + '\n'
            elif self.__create in line:
                output += self.get_create(model_object)
            elif self.__search in line:
                output += self.get_search(list_of_objects)
            elif self.__info in line:
                output += self.get_info(model_object)
        return output
                
    def get_spaceing(self, file = '', graphics = '', model_object = '', list_of_objects = ''):
        counter = 3
        output = ''
        for line in self.get_file(file):
            if self.__graphics in line:
                for line in self.get_file(graphics):
                    counter += 1
            elif self.__create in line:
                for line in self.get_create(model_object).splitlines():
                    counter += 1
            elif self.__search in line:
                for line in self.get_search(list_of_objects).splitlines():
                    counter += 1
            elif self.__info in line:
                for line in self.get_info(model_object).splitlines():
                    counter += 1
            else:
                counter += 1
        for i in range(self.__window_height - counter):
            left_border = (self.__space * 4) + self.__vertical
            contents = self.__space * (self.__window_width - 10)
            right_border = self.__vertical
            output += '{}{}{}'.format(left_border, contents, right_border) + '\n'
        return output

    def get_info(self, model_object):
        output = ''
        temp = self.display_search_object(model_object).splitlines()        
        for line in temp:
            left_border = (self.__space * 4) + self.__vertical
            contents = (self.__space * 5) + line.ljust(self.__window_width - 15)
            right_border = self.__vertical
            output += '{}{}{}'.format(left_border, contents, right_border) + '\n'
        return output
    
    def get_create(self, model_object):
        output = ''      
        temp = self.display_model_object(model_object).splitlines()
        for line in temp:
            left_border = (self.__space * 4) + self.__vertical
            contents = (self.__space * 5) + line.ljust(self.__window_width - 15)
            right_border = self.__vertical
            output += '{}{}{}'.format(left_border, contents, right_border) + '\n'
        return output
    
    def get_search(self, list_of_objects):
        output = ''      
        temp = self.search_model_object(list_of_objects).splitlines()
        for line in temp:
            left_border = (self.__space * 4) + self.__vertical
            contents = (self.__space * 5) + line.ljust(self.__window_width - 15)
            right_border = self.__vertical
            output += '{}{}{}'.format(left_border, contents, right_border) + '\n'
        return output

    def get_file_contents(self, file):
        output = ''
        for line in self.get_file(file):
            left_border = (self.__space * 4) + self.__cross
            contents = line.center(self.__window_width - 10, self.__horizontal)
            right_border = self.__cross
            output += '{}{}{}'.format(left_border, contents, right_border) + '\n'
        return output
        
    def get_fact(self, facts):        
        _facts = self.get_file(facts)
        fact = _facts[random.randint(0,len(_facts))]
        left_border = (self.__space * 4) + self.__vertical
        contents = ('...'+fact).rjust(self.__window_width-15) + (self.__space * 5)
        right_border = self.__vertical
        return '{}{}{}'.format(left_border, contents, right_border)
            
    def get_centerJust(self, line):
        left_border = (self.__space * 4) + self.__vertical
        contents = line.replace(self.__center_just, '').center(self.__window_width - 10)
        right_border = self.__vertical
        return '{}{}{}'.format(left_border, contents, right_border)

    def get_rightJust_indent(self, line):
        left_border = (self.__space * 4) + self.__vertical
        contents = line.replace(self.__right_just+self.__indent, '').rjust(self.__window_width -15) + (self.__space * 5)
        right_border = self.__vertical
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_rightJust(self, line):
        left_border = (self.__space * 4) + self.__vertical
        contents = line.replace(self.__right_just, '').rjust(self.__window_width -10)
        right_border = self.__vertical
        return '{}{}{}'.format(left_border, contents, right_border)

    def get_leftJust_indent(self, line):
        left_border = (self.__space * 4) + self.__vertical
        contents = (self.__space * 5) + line.replace(self.__left_just+self.__indent, '').ljust(self.__window_width -15)
        right_border = self.__vertical
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_leftJust(self, line):
        left_border = (self.__space * 4) + self.__vertical
        contents = line.replace(self.__left_just, '').ljust(self.__window_width -10)
        right_border = self.__vertical
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_seperator(self):
        left_border = (self.__space * 4) + self.__cross
        contents = (self.__horizontal * (self.__window_width - 10))
        right_border = self.__cross
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_emptyline(self):
        left_border = (self.__space * 4) + self.__vertical
        contents = (self.__space * (self.__window_width - 10))
        right_border = self.__vertical
        return '{}{}{}'.format(left_border, contents, right_border)
    
    def get_breadcrumbs(self, address):
        left_border = (self.__space * 4) + self.__vertical
        contents = (self.__space * 5) + address + (self.__space *(self.__window_width-len(address)-15))
        right_border = self.__vertical
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
            
    def multi_select(self):
        _input = self.multi_input()        
        output = False                
        for item in self.OPTIONS:
            if _input == item[0]:
                output = item[1]
        for key, value in self.__menus.items():
            if output == key:
                output = value
        return (_input, output)   

    def select_fromMenu(self):                
        _input = self.single_input()                                  
        output = False                
        for item in self.OPTIONS:
            if _input == item[0]:
                output = item[1]
        for key, value in self.__menus.items():
            if output == key:
                output = value        
        return (_input, output)        

    def validate_selection(self, class_name):
        print('Enter your selction:')
        if self.SCREEN_TYPE == 'Menu':
            user_input = self.select_fromMenu()
        else: 
            user_input = self.multi_select()        
        while not user_input[1]:
            print(self.prep_window(class_name.FILE, class_name.GRAPHICS_FILE))
            print('Invalid selection, please try again:')
            user_input = self.select_fromMenu()        
        return user_input