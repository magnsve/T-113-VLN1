# Imports and constants
from .il_trips_menu import IL_TripsMenu

# Classes
class IL_TripsCreateMenu(IL_TripsMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Trips -> New Trip'
    SCREEN_TYPE = 'Create'
    CATEGORY = 'Trips'
    OPTIONS = [('1','M_4_1_1'),('2','M_4_1_2'),('3', 'M_4_1_3'),('4','M_4_1_4'),('r','M_4_1'),('q','Q'),('b','M_4')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_TripsMenu'
        self.__module = 'il_trips_create_menu'
        self.__class_name = 'IL_TripsCreateMenu'