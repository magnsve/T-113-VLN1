# Imports and constants
from .il_main_menu import IL_MainMenu
from LogicLayer.ll_api import LL_API

# Classes
class IL_SelectScreen(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> Find Employee'
    SCREEN_TYPE = 'Search'
    OPTIONS = [('r','M_1_2','Screen'),('q','Q','Screen'),('b','M_1','Screen'),('s','M_select','Screen')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_EmployeeMenu'
        self.__module = 'il_employee_search_menu'
        self.__class_name = 'IL_EmployeeSearchMenu'