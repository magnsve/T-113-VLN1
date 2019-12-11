# Imports and constants
from .il_destination_search_menu import IL_DestinationSearchMenu

# Classes
class IL_DestinationListMenu(IL_DestinationSearchMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationListMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationList_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> Find Destination -> List of Destinations'
    SCREEN_TYPE = 'List'
    CATEGORY = 'Destination'
    OPTIONS = [('r','M_3_2_2','Screen'),('q','Q','Screen'),('b','M_3_2','Screen')]