# Imports and constants
from .il_airplane_search_menu import IL_AirplaneSearchMenu

# Classes
class IL_AirplaneEditMenu(IL_AirplaneSearchMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneEditMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneEdit_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> Find Airplane -> Edit Airplane'
    SCREEN_TYPE = 'Edit'
    CATEGORY = 'Plane'
    OPTIONS = [('r','M_2_2_1','Screen'),('q','Q','Screen'),('b','M_2_2','Screen'),('x','X','Reset')]