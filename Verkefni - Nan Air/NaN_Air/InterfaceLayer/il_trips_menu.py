# Imports and constants
from .il_main_menu import IL_MainMenu

# Classes
class IL_TripsMenu(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Trips'
    SCREEN_TYPE = 'Menu'
    CATEGORY = 'Trip'
    OPTIONS = [('1','M_4_1','Screen'),('2','M_4_2','Screen'),('r','M_4','Screen'),('q','Q','Screen'),('b','M','Screen')]