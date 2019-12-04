# Imports and constants
from .IL_MainMenu import IL_MainMenu

# Classes
class IL_AirplaneMenu(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Airplane Menu'
    PARENT = 'IL_MainMenu'
    YOU_ARE_HERE = 'IL_AirplaneMenu'    
    OPTIONS = [('1','M_2_1'),('2','M_2_2'),('r','M_2'),('q','Q'),('b','M')]