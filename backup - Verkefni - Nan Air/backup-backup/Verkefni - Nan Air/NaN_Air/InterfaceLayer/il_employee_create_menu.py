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
    OPTIONS = [('1','M_1_1_1'),('2','M_1_1_2'),('3','M_1_1_3'),('4','M_1_1_4'),('r','M_1_1'),('q','Q'),('b','M_1')]

    def __init__(self):
        super().__init__()        
        self.__parent_class = 'IL_EmployeeMenu'
        self.__module = 'il_employee_create_menu'
        self.__class_name = 'IL_EmployeeCreateMenu'               
    
    def display_model_object(self, employee_object = None):        
        if employee_object:            
            ssn = '1 - SSN: {}'.format(employee_object.get_ssn())
            name = '2 - Name: {}'.format(employee_object.get_name())
            role = '3 - Role: {}'.format(employee_object.get_role())
            rank = '4 - Rank: {}'.format(employee_object.get_rank())
            licence = '5 - Licence: {}'.format(employee_object.get_licence())
            address = '6 - Address: {}'.format(employee_object.get_address())
            phonenumber = '7 - Phonenumber: {}'.format(employee_object.get_phonenumber())
            status = '8 - Status: {}'.format(employee_object.get_status())
            return [ssn, name, role, rank, licence, address, phonenumber, status]
        else:
            return ''