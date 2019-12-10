# Imports and constants
from .il_employee_menu import IL_EmployeeMenu

# Classes
class IL_EmployeeCreateMenu(IL_EmployeeMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> New Employee'
    SCREEN_TYPE = 'Create'
    CATEGORY = 'Employee'
    OPTIONS = [ ('r','M_1_1','Screen'),('q','Q','Screen'),('b','M_1','Screen'),('x','X','Reset')]