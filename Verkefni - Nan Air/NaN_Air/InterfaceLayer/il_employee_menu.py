# Imports and constants
from .il_main_menu import IL_MainMenu

# Classes
class IL_EmployeeMenu(IL_MainMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Employees'
    SCREEN_TYPE = 'Menu'
    CATEGORY = 'Employee'
    OPTIONS = [('1','M_1_1','Screen'),('2','M_1_2','Screen'),('r','M_1','Screen'),('q','Q','Screen'),('b','M','Screen')]