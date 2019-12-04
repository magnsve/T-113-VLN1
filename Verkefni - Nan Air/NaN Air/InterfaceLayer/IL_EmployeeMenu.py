# Imports and constants
from IL_MainMenu import IL_MainMenu

# Classes
class IL_EmployeeMenu(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Employee Menu'
    PARENT = 'IL_MainMenu'
    YOU_ARE_HERE = 'IL_EmployeeMenu'    
    OPTIONS = [('1','M_1_1'),('2','M_1_2'),('r','M_1'),('q','Q'),('b','M')]