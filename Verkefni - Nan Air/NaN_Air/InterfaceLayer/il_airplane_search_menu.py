# Imports and constants
from .il_airplane_menu import IL_AirplaneMenu

# Classes
class IL_AirplaneSearchMenu(IL_AirplaneMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> Find Airplane'
    PARENT = 'il_airplane_menu'
    YOU_ARE_HERE = 'il_airplane_search_menu'    
    OPTIONS = [('1','M_2_2_1'),('2','M_2_2_2'),('3','M_2_2_3'),('4','M_2_2_4'),('5','M_2_2_5'),('6','M_2_2_6'),('r','M_2_2'),('q','Q'),('b','M_2')]

    def __init__(self):
        self.__parent_class = 'IL_AirplaneMenu'
        self.__module = 'il_airplane_search_menu'
        self.__class_name = 'IL_AirplaneSearchMenu'
        super().__init__()