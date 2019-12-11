# Imports and constants
from .il_employee_search_menu import IL_EmployeeSearchMenu

# Classes
class IL_EmployeeEditMenu(IL_EmployeeSearchMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeEditMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeEdit_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> Find Employee -> Edit Employee'
    SCREEN_TYPE = 'Edit'
    CATEGORY = 'Employee'
    OPTIONS = [('r','M_1_2_1','Screen'),('q','Q','Screen'),('b','M_1_2','Screen'),('x','X','Reset')]