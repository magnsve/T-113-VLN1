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
    OPTIONS = [('r','M_1_2','Screen'),('q','Q','Screen'),('b','M_1','Screen'),('x','X','Reset')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_EmployeeMenu'
        self.__module = 'il_employee_search_menu'
        self.__class_name = 'IL_EmployeeSearchMenu'