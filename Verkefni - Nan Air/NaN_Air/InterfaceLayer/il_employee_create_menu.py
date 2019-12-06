# Imports and constants
from .il_employee_menu import IL_EmployeeMenu

# Classes
class IL_EmployeeCreateMenu(IL_EmployeeMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> New Employee'
    OPTIONS = [('1','M_1_1_1'),('2','M_1_1_2'),('3','M_1_1_3'),('4','M_1_1_4'),('r','M_1_1'),('q','Q'),('b','M_1')]

    def __init__(self):
        self.__parent_class = 'IL_EmployeeMenu'
        self.__module = 'il_employee_create_menu'
        self.__class_name = 'IL_EmployeeCreateMenu'
        super().__init__()