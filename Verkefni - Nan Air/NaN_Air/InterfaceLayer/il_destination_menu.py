# Imports and constants
from .il_main_menu import IL_MainMenu

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
        self.__screen_type = 'Menu'
        self.__category = 'Destination'
        super().__init__()