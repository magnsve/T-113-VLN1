# Imports and constants
from .il_destination_search_menu import IL_DestinationSearchMenu

# Classes
class IL_DestinationEditMenu(IL_DestinationSearchMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationEditMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationEdit_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> Find Destination -> Edit Destination'
    SCREEN_TYPE = 'Edit'
    CATEGORY = 'Destination'
    OPTIONS = [('r','M_3_2_1','Screen'),('q','Q','Screen'),('b','M_3_2','Screen'),('x','X','Reset')]