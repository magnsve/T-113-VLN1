# Imports and constants
from .il_destination_menu import IL_DestinationMenu

# Classes
class IL_DestinationSearchMenu(IL_DestinationMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> Find Destination'
    SCREEN_TYPE = 'Search'
    CATEGORY = 'Destination'
    OPTIONS = [('1','M_3_2_1'),('2','M_3_2_1'),('r','M_3_2'),('q','Q'),('b','M_3')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_DestinationMenu'
        self.__module = 'il_destination_search_menu'
        self.__class_name = 'IL_DestinationSearchMenu'