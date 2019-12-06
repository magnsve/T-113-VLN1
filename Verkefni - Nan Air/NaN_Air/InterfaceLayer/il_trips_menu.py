# Imports and constants
from .il_main_menu import IL_MainMenu

# Classes
class IL_TripsMenu(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Trips'
    PARENT = 'IL_MainMenu'
    YOU_ARE_HERE = 'IL_TripsMenu'    
    OPTIONS = [('1','M_4_1'),('2','M_4_2'),('r','M_4'),('q','Q'),('b','M')]