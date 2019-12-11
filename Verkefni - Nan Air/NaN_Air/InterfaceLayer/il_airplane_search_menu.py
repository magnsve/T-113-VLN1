# Imports and constants
from .il_airplane_menu import IL_AirplaneMenu

# Classes
class IL_AirplaneSearchMenu(IL_AirplaneMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> Find Airplane'
    SCREEN_TYPE = 'Search'
    CATEGORY = 'Plane' 
    OPTIONS = [('r','M_2_2','Screen'),('q','Q','Screen'),('b','M_2','Screen'),('list','L','Screen'),('x','X','Reset')]