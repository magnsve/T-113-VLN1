# Imports and constants
from .il_destination_menu import IL_DestinationMenu

# Classes
class IL_DestinationCreateMenu(IL_DestinationMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> New Destination'
    SCREEN_TYPE = 'Create'
    CATEGORY = 'Destination' 
    OPTIONS = [('r','M_3_1','Screen'),('q','Q','Screen'),('b','M_3','Screen'),('x','X','Reset')]