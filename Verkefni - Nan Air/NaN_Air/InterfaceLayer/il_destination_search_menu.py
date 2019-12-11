# Imports and constants
from .il_destination_menu import IL_DestinationMenu

# Classes
class IL_DestinationSearchMenu(IL_DestinationMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> Find Destination'
    SCREEN_TYPE = 'Search'
    CATEGORY = 'Destination'
    OPTIONS = [('r','M_3_2','Screen'),('q','Q','Screen'),('b','M_3','Screen'),('list','L','Screen'),('x','X','Reset')]