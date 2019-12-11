# Imports and constants
from .il_airplane_search_menu import IL_AirplaneSearchMenu

# Classes
class IL_AirplaneListMenu(IL_AirplaneSearchMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneListMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneList_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> Find Airplane -> List of Planes'
    SCREEN_TYPE = 'List'
    CATEGORY = 'Plane'
    OPTIONS = [('r','M_2_2_2','Screen'),('q','Q','Screen'),('b','M_2_2','Screen')]