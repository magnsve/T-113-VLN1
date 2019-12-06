# Imports and constants
from .IL_MainMenu import IL_MainMenu

# Classes
class IL_DestinationMenu(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations'
    OPTIONS = [('1','M_3_1'),('2','M_3_2'),('r','M_3'),('q','Q'),('b','M')]

    def __init__(self):
        self.__parent_class = 'IL_MainMenu'
        self.__module = 'il_destination_menu'
        self.__class_name = 'IL_DestinationMenu'
        super().__init__()