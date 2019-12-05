# Imports and constants
from .IL_TripsMenu import IL_TripsMenu

# Classes
class IL_TripsCreateMenu(IL_TripsMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Trips -> New Trip'
    PARENT = 'IL_TripsMenu'
    YOU_ARE_HERE = 'IL_TripsCreateMenu'    
    OPTIONS = [('1','M_4_1_1'),('2','M_4_1_2'),('3', 'M_4_1_3'),('4','M_4_1_4'),('r','M_4_1'),('q','Q'),('b','M_4')]