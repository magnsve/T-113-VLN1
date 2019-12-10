# Imports and constants
from .il_airplane_menu import IL_AirplaneMenu

# Classes
class IL_AirplaneSearchMenu(IL_AirplaneMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> Find Airplane'
    SCREEN_TYPE = 'Search'
    CATEGORY = 'Planes' 
    OPTIONS = [('r','M_2_2','Screen'),('q','Q','Screen'),('b','M_2','Screen'),('x','X','Reset')]