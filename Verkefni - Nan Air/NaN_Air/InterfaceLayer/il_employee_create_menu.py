# Imports and constants
from .il_employee_menu import IL_EmployeeMenu
from LogicLayer.ll_api import LL_API

# Classes
class IL_EmployeeCreateMenu(IL_EmployeeMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> New Employee'
    SCREEN_TYPE = 'Create'
    CATEGORY = 'Employee'
    OPTIONS = [ ('1','M_1_1_1','Screen'),('2','M_1_1_2','Screen'),('3','M_1_1_3','Screen'),('4','M_1_1_4','Screen'),('r','M_1_1','Screen'),\
                ('q','Q','Screen'),('b','M_1','Screen')]

    def __init__(self):
        super().__init__()        
        self.__parent_class = 'IL_EmployeeMenu'
        self.__module = 'il_employee_create_menu'
        self.__class_name = 'IL_EmployeeCreateMenu'
        
    def display_model_object(self, employee_object = None):
        output = ''
        header_row = LL_API().get_employee_header()
        item_values = employee_object.__dict__.values()
        column_width = 65
        counter = 0
        for index, item in enumerate(item_values):            
            if header_row[index] == 'history':
                continue
            else:
                output += '{} - {}: {}'.format(index+1,header_row[index].capitalize(),item).ljust(column_width)
                counter += 1
                if counter == 2:
                    output += '\n'
                    counter = 0
        return output
    