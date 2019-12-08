# Imports and constants
from .il_trips_menu import IL_TripsMenu

# Classes
class IL_TripsSearchMenu(IL_TripsMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Trips -> Find Trip'
    SCREEN_TYPE = 'Search'
    CATEGORY = 'Trips'
    OPTIONS = [('1','M_4_2_1'),('2','M_4_2_2'),('3', 'M_4_2_3'),('4','M_4_2_4'),('r','M_4_2'),('q','Q'),('b','M_4')]
    
    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_TripsMenu'
        self.__module = 'il_trips_search_menu'
        self.__class_name = 'IL_TripsSearchMenu'