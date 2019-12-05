# Imports and constants
from .IL_DestinationMenu import IL_DestinationMenu

# Classes
class IL_DestinationCreateMenu(IL_DestinationMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> New Destination'
    PARENT = 'IL_Destination'
    YOU_ARE_HERE = 'IL_DestinationsCreateMenu'    
    OPTIONS = [('1','M_3_1_1'),('2','M_3_1_2'),('r','M_3_1'),('q','Q'),('b','M_3')]