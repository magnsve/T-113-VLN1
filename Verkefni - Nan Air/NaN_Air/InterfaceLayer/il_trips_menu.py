# Imports and constants
from .il_main_menu import IL_MainMenu

# Classes
class IL_TripsMenu(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Trips'
    OPTIONS = [('1','M_4_1'),('2','M_4_2'),('r','M_4'),('q','Q'),('b','M')]

    def __init__(self):
        self.__parent_class = 'IL_MainMenu'
        self.__module = 'il_trips_menu'
        self.__class_name = 'IL_TripsMenu'
        super().__init__()