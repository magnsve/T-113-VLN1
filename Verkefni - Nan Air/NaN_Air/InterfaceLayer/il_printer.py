# Imports and constants
import sys, os, shutil, random, datetime
from msvcrt import getch
from importlib import import_module, invalidate_caches
from LogicLayer.ll_api import LL_API

# Classes
class IL_Printer():
    ''' This class initializes the TUI window and determines what data should be displayed. The class speaks with the Logic layer API.
    This class has one major method and several minor methods. Prep_window calls several minor methods to determine the size, width, spacing
    and contents of the window. 
    '''
    FILE = ''
    GRAPHICS_FILE =  ''
    
    def __init__(self):
        #Initalises window
        self.__window_width = shutil.get_terminal_size()[0]
        self.__window_height = shutil.get_terminal_size()[1]        
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
        self.__menus = {'M':('il_main_menu','IL_MainMenu'),'M_1':('il_employee_menu','IL_EmployeeMenu'),'M_1_1':('il_employee_create_menu','IL_EmployeeCreateMenu'),'M_1_2':('il_employee_search_menu','IL_EmployeeSearchMenu'),'M_1_2_1':('il_employee_edit_menu','IL_EmployeeEditMenu'),'M_1_2_2':('il_employee_list_menu','IL_EmployeeListMenu'),'M_2':('il_airplane_menu','IL_AirplaneMenu'),'M_2_1':('il_airplane_create_menu','IL_AirplaneCreateMenu'),'M_2_2':('il_airplane_search_menu','IL_AirplaneSearchMenu'),'M_2_2_1':('il_airplane_edit_menu','IL_AirplaneEditMenu'),'M_2_2_2':('il_airplane_list_menu','IL_AirplaneListMenu'),'M_3':('il_destination_menu','IL_DestinationMenu'),'M_3_1':('il_destination_create_menu','IL_DestinationCreateMenu'),'M_3_2':('il_destination_search_menu','IL_DestinationSearchMenu'),'M_3_2_1':('il_destination_edit_menu','IL_DestinationEditMenu'),'M_3_2_2':('il_destination_list_menu','IL_DestinationListMenu'),'M_4':('il_trips_menu','IL_TripsMenu'),'M_4_1':('il_trips_create_menu','IL_TripsCreateMenu'),'M_4_2':('il_trips_search_menu','IL_TripsSearchMenu'),'M_4_2_1':('il_trips_edit_menu','IL_TripsEditMenu'),'M_4_2_2':('il_trips_list_menu','IL_TripsListMenu'),'Q':('il_quit_screen','IL_QuitScreen'),'M_1_2_1':('il_employee_edit_menu','IL_EmployeeEditMenu')}
    
    def variable_class(self, from_menu = ('','')):
        module_name = 'InterfaceLayer.'+ from_menu[0]
        class_name = from_menu[1]
        module = import_module(module_name)
        class_ = getattr(module, class_name)        
        return class_()
    
    def prep_window(self, file = FILE, graphics = GRAPHICS_FILE, model_object = None, list_of_objects = None, period = None):
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
            elif self.__criteria in line:
                output += self.get_criteria(period)
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
        temp = self.display_model_object(model_object).splitlines()        
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
        fact = _facts[random.randint(0,len(_facts)-1)]
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
    
    def single_input(self):        
        try:
            return getch().decode('ASCII').lower()
        except UnicodeDecodeError:
            return 'z'
    
    def multi_input(self):
        return input().lower()
            
    def multi_select(self, list_of_objects= None):
        _input = self.multi_input()
        output = False        
        for item in self.OPTIONS:
            if _input == item[0]:
                output = item[1]
        for key, value in self.__menus.items():
            if output == key:
                output = value
        try:
            if list_of_objects == None:
                pass
            elif not 0 < int(_input) <= len(list_of_objects):            
                output = False
        except ValueError:
            pass
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

    def validate_selection(self, class_name, model_class_object = None, list_of_objects = None):
        print('Enter your selction:')
        _type = self.SCREEN_TYPE
        if _type == 'Menu':
            user_input = self.select_fromMenu()
        else:            
            user_input = self.multi_select(list_of_objects)
        while not user_input[1]:
            print(self.prep_window(class_name.FILE, class_name.GRAPHICS_FILE, model_class_object, list_of_objects))
            print('Invalid selection, please try again:')
            if _type == 'Menu':
                user_input = self.select_fromMenu()
            else: 
                user_input = self.multi_select(list_of_objects)
        return user_input

    def reset_object(self, model_class_object):
        return model_class_object.__init__()

    def list_of_get_functions(self, model_class_object):
        return [func for func in dir(model_class_object) if callable(getattr(model_class_object, func)) and func.startswith("get")]
    
    def list_of_set_functions(self, logic_layer_object):
        return [func for func in dir(logic_layer_object) if callable(getattr(logic_layer_object, func)) and func.startswith("ll_set")]
    
    def get_edit_funcs(self, logic_layer_object):
        ''' This function adds options to the self.OPTIONS of the class that calls it. 
        The options correspond to the available 'set' functions for the model_class_object. '''
        options_list = []
        options = self.list_of_set_functions(logic_layer_object)
        for index, item in enumerate(options):
            options_list.append(('e' + str(index + 1), item,'Func'))
        for item in options_list:
            self.OPTIONS.append(item)
    
    def get_list_options(self, list_of_objects):
        ''' This function adds options to the self.OPTIONS of the class that calls it. 
        The options correspond to the number of items in the list_of_objects. '''
        options_list = []        
        for i in range(len(list_of_objects[:10])):
            options_list.append((str(i+1),str(i),'Lists'))
        for item in options_list:
            self.OPTIONS.append(item)
    
    def get_select_options(self, list_of_objects):
        ''' This function adds options to the self.OPTIONS of the class that calls it. 
        The options correspond to the available objects in the list_of_objects. '''
        options_list = []
        for i in range(len(list_of_objects[:10])):
            options_list.append(('s'+str(i+1),'s'+str(i),'Select'))
        for item in options_list:
            self.OPTIONS.append(item)    

    def display_model_object(self, model_class_object = None):
        ''' This function creates a string to display the values in the model_class_object. '''
        output = ''
        method_ = getattr(LL_API(), "get_"+self.CATEGORY.lower()+"_header")
        header_row = method_()
        header_row.sort()
        item_values = model_class_object.__dict__
        sorted(item_values)
        #column_width = (self.__window_width - 30) // (len(header_row)+1)
        column_width = 40
        counter = 0
        for index, item in enumerate(header_row):
            if item == 'e-mail':
                item = 'e_mail'            
            output += 'E{} {}: {}'.format(index+1,item.replace('e_mail','e-mail').upper(),item_values['_'+self.CATEGORY+"__"+item.replace(' ','_').replace('.','')]).ljust(column_width)
            counter += 1
            if counter == 3:
                output += '\n'
                counter = 0
        return output
    
    def search_model_object(self, list_of_objects = None):
        ''' This function creates a string to display the search results from the list_of_objects. '''
        method_ = getattr(LL_API(), "get_"+self.CATEGORY.lower()+"_header")
        header_row = method_()
        column_width = (self.__window_width - 30) // (len(header_row))
        output = 'No'.center(10)
        for item in header_row:
            if len(item) > (column_width - 1):
                output += (item.upper()[0:(column_width-5)] + '...').ljust(column_width)
            else:
                output += item.upper().ljust(column_width)            
        output += '{}{}{}'.format('\n','-'*(self.__window_width - 20),'\n')
        for index, item in enumerate(list_of_objects):
            item_values = item.__dict__.values()            
            string = '{}'.format(index+1).center(10)
            for element in item_values:
                if len(element) > (column_width - 1):
                    string += (element[0:(column_width-5)] + '...').ljust(column_width)
                else:
                    string += element.ljust(column_width)
            output += string + '\n'
        output += '\n'
        output += 'Search returned {} results.\n'.format(len(list_of_objects)).center(self.__window_width - 20)
        return output