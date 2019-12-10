# Imports and constants
from .il_trips_search_menu import IL_TripsSearchMenu

# Classes
class IL_TripsEditMenu(IL_TripsSearchMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsEditMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsEdit_graphics.txt'
    ADDRESS = 'Main Menu -> Trips -> Find Trip -> Edit Trips'
    SCREEN_TYPE = 'Edit'
    CATEGORY = 'Trip'
    OPTIONS = [('r','M_4_2_1','Screen'),('q','Q','Screen'),('b','M_4_2','Screen'),('x','X','Reset')]