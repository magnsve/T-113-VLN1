# Imports and constants
from .il_employee_menu import IL_EmployeeMenu

# Classes
class IL_EmployeeSearchMenu(IL_EmployeeMenu):
    '''Creates Airplane menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> Find Employee'
    SCREEN_TYPE = 'Search'
    CATEGORY = 'Employee'
    OPTIONS = [('r','M_1_2','Screen'),('q','Q','Screen'),('b','M_1','Screen'),('list','L','Screen'),('x','X','Reset')]