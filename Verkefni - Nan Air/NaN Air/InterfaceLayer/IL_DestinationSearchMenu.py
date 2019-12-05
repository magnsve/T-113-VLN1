# Imports and constants
from .IL_DestinationMenu import IL_DestinationMenu

# Classes
class IL_DestinationSearchMenu(IL_DestinationMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> Find Destination'
    PARENT = 'IL_Destination'
    YOU_ARE_HERE = 'IL_DestinationsSearchMenu'    
    OPTIONS = [('1','M_3_2_1'),('2','M_3_2_1'),('r','M_3_2'),('q','Q'),('b','M_3')]