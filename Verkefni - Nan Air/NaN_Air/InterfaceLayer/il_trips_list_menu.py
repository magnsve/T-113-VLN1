# Imports and constants
from .il_trips_search_menu import IL_TripsSearchMenu

# Classes
class IL_TripsListMenu(IL_TripsSearchMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsListMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsList_graphics.txt'
    ADDRESS = 'Main Menu -> Trips -> Find Trip -> List of Trips'
    SCREEN_TYPE = 'List'
    CATEGORY = 'Trip'
    OPTIONS = [('r','M_4_2_2','Screen'),('q','Q','Screen'),('b','M_4_2','Screen')]