# Imports and constants
from .il_destination_menu import IL_DestinationMenu

# Classes
class IL_DestinationCreateMenu(IL_DestinationMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> New Destination'
    SCREEN_TYPE = 'Create'
    CATEGORY = 'Destination' 
    OPTIONS = [('1','M_3_1_1'),('2','M_3_1_2'),('r','M_3_1'),('q','Q'),('b','M_3')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_DestinationMenu'
        self.__module = 'il_destination_create_menu'
        self.__class_name = 'IL_DestinationCreateMenu'