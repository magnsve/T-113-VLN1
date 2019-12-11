# Imports and constants
from .il_trips_menu import IL_TripsMenu

# Classes
class IL_TripsSearchMenu(IL_TripsMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Trips -> Find Trip'
    SCREEN_TYPE = 'Search'
    CATEGORY = 'Trip'
    OPTIONS = [('r','M_4_2','Screen'),('q','Q','Screen'),('b','M_4','Screen'),('list','L','Screen'),('x','X','Reset')]    