# Imports and constants
from .il_main_menu import IL_MainMenu
from ModelClasses.employee import Employee
from LogicLayer.ll_api import LL_API

# Classes
class IL_EmployeeMenu(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Employees'
    SCREEN_TYPE = 'Menu'
    CATEGORY = 'Employee'
    OPTIONS = [('1','M_1_1'),('2','M_1_2'),('r','M_1'),('q','Q'),('b','M')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_MainMenu'
        self.__module = 'il_employee_menu'
        self.__class_name = 'IL_EmployeeMenu'