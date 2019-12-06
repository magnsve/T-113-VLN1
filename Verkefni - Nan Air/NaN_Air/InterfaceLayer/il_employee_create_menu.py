# Imports and constants
from .il_employee_menu import IL_EmployeeMenu

# Classes
class IL_EmployeeCreateMenu(IL_EmployeeMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> New Employee'
    PARENT = 'IL_EmployeeMenu'
    YOU_ARE_HERE = 'IL_EmployeeCreateMenu'
    OPTIONS = [('1','M_1_1_1'),('2','M_1_1_2'),('3','M_1_1_3'),('4','M_1_1_4'),('r','M_1_1'),('q','Q'),('b','M_1')]