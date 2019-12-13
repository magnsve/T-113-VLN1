# Imports and constants
from .il_trips_menu import IL_TripsMenu

# Classes
class IL_TripsCreateMenu(IL_TripsMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Trips -> New Trip'
    SCREEN_TYPE = 'Create'
    CATEGORY = 'Trip'    
    OPTIONS = [('r','M_4_1','Screen'),('q','Q','Screen'),('b','M_4','Screen'),('x','X','Reset')]