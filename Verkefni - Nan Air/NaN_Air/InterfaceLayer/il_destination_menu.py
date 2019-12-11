# Imports and constants
from .il_main_menu import IL_MainMenu

# Classes
class IL_DestinationMenu(IL_MainMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations'
    SCREEN_TYPE = 'Menu'
    CATEGORY = 'Destination' 
    OPTIONS = [('1','M_3_1','Screen'),('2','M_3_2','Screen'),('r','M_3','Screen'),('q','Q','Screen'),('b','M','Screen')]