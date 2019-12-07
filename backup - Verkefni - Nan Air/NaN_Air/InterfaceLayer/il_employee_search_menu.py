# Imports and constants
from .il_employee_menu import IL_EmployeeMenu

# Classes
class IL_EmployeeSearchMenu(IL_EmployeeMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> Find Employee'
    OPTIONS = [('1','M_1_2_1'),('2','M_1_2_2'),('3','M_1_2_3'),('4','M_1_2_4'),('5','M_1_2_5'),('6','M_1_2_6'),('r','M_1_2'),('q','Q'),('b','M_1')]

    def __init__(self):
        self.__parent_class = 'IL_EmployeeMenu'
        self.__module = 'il_employee_search_menu'
        self.__class_name = 'IL_EmployeeSearchMenu'
        self.__screen_type = 'Search'
        self.__category = 'Employee'
        super().__init__()