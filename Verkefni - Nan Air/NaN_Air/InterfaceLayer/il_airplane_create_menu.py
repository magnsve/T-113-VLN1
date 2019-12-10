# Imports and constants
from .il_airplane_menu import IL_AirplaneMenu

# Classes
class IL_AirplaneCreateMenu(IL_AirplaneMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> New Airplane'
    SCREEN_TYPE = 'Create'
    CATEGORY = 'Plane' 
    OPTIONS = [ ('r','M_2_1','Screen'),('q','Q','Screen'),('b','M_2','Screen'),('x','X','Reset')]    