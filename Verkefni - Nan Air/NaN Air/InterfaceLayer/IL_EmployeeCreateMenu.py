# Imports and constants
from .IL_EmployeeMenu import IL_EmployeeMenu

# Classes
class IL_EmployeeCreateMenu(IL_EmployeeMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Employee Menu -> New Employee'
    PARENT = 'IL_EmployeeMenu'
    YOU_ARE_HERE = 'IL_EmployeeCreateMenu'
    OPTIONS = [('1','M_1_1_1'),('2','M_1_1_2'),('3','M_1_1_3'),('4','M_1_1_4'),('r','M_1_1'),('q','Q'),('b','M_1')]