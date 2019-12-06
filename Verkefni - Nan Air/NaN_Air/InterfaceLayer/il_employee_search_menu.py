# Imports and constants
from .il_employee_menu import IL_EmployeeMenu

# Classes
class IL_EmployeeSearchMenu(IL_EmployeeMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> Find Employee'
    PARENT = 'IL_EmployeeMenu'
    YOU_ARE_HERE = 'IL_EmployeeSearchMenu'
    OPTIONS = [('1','M_1_2_1'),('2','M_1_2_2'),('3','M_1_2_3'),('4','M_1_2_4'),('5','M_1_2_5'),('6','M_1_2_6'),('r','M_1_2'),('q','Q'),('b','M_1')]