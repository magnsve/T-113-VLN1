# Imports and constants
from .il_employee_search_menu import IL_EmployeeSearchMenu

# Classes
class IL_EmployeeListMenu(IL_EmployeeSearchMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeListMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeList_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> Find Employee -> List of Employees'
    SCREEN_TYPE = 'List'
    CATEGORY = 'Employee'
    OPTIONS = [('r','M_1_2_2','Screen'),('q','Q','Screen'),('b','M_1_2','Screen')]