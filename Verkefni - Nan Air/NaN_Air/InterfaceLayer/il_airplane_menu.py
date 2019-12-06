# Imports and constants
from .il_main_menu import IL_MainMenu

# Classes
class IL_AirplaneMenu(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneMenu_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes'
    OPTIONS = [('1','M_2_1'),('2','M_2_2'),('r','M_2'),('q','Q'),('b','M')]

    def __init__(self):
        self.__parent_class = 'IL_MainMenu'
        self.__module = 'il_airplane_menu'
        self.__class_name = 'IL_AirplaneMenu'
        super().__init__()