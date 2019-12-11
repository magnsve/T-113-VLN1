# Imports and constants
from .il_main_menu import IL_MainMenu

# Classes
class IL_AirplaneMenu(IL_MainMenu):
    '''Creates menu pulling info from UI_MetaData '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes'    
    SCREEN_TYPE = 'Menu'
    CATEGORY = 'Plane' 
    OPTIONS = [('1','M_2_1','Screen'),('2','M_2_2','Screen'),('r','M_2','Screen'),('q','Q','Screen'),('b','M','Screen')]