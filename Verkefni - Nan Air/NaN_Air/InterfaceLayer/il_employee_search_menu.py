# Imports and constants
from .il_employee_menu import IL_EmployeeMenu
from LogicLayer.ll_api import LL_API

# Classes
class IL_EmployeeSearchMenu(IL_EmployeeMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> Find Employee'
    SCREEN_TYPE = 'Search'
    CATEGORY = 'Employee'
    OPTIONS = [('r','M_1_2'),('q','Q'),('b','M_1')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_EmployeeMenu'
        self.__module = 'il_employee_search_menu'
        self.__class_name = 'IL_EmployeeSearchMenu'

    def get_input_optins(self, employee_object = None):        
        options_list = []
        options = LL_API().get_employee_header()
        for index, item in enumerate(options):
            options_list.append(('E' + str(index+1), 'set_' + item))
        return options_list
    
    def display_search_object(self, employee_object = None):
        output = ''
        header_row = LL_API().get_employee_header()
        item_values = employee_object.__dict__.values()
        column_width = 40
        counter = 0
        for index, item in enumerate(item_values):
            output += 'E{} {}: {}'.format(index+1,header_row[index].upper(),item).ljust(column_width)
            counter += 1
            if counter == 3:
                output += '\n'
                counter = 0
        return output
    
    def search_model_object(self, list_of_objects = None):
        header_row = LL_API().get_employee_header()
        column_width = 130 // (len(header_row)+1)
        output = 'No'.center(column_width)
        for item in header_row:
            output += item.upper().ljust(column_width)
        output += '{}{}{}'.format('\n','-'*130,'\n')
        for index, item in enumerate(list_of_objects):
            item_values = item.__dict__.values()            
            string = '{}'.format(index+1).center(column_width)
            for element in item_values:
                if len(element) > (column_width - 1):
                    string += (element[0:(column_width-5)] + '...').ljust(column_width)
                else:
                    string += element.ljust(column_width)
            output += string + '\n'        
        return output