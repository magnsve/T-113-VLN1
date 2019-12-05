# Imports and constants
from .IL_TripsMenu import IL_TripsMenu

# Classes
class IL_TripsSearchMenu(IL_TripsMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/TripsSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/TripsSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Trips -> Find Trip'
    PARENT = 'IL_TripsMenu'
    YOU_ARE_HERE = 'IL_TripsSearchMenu'
    OPTIONS = [('1','M_4_2_1'),('2','M_4_2_2'),('3', 'M_4_2_3'),('4','M_4_2_4'),('r','M_4_2'),('q','Q'),('b','M_4')]