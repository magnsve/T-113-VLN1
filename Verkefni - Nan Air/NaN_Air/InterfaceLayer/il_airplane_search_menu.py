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
    OPTIONS = [ ('1','M_2_2_1','Screen'),('2','M_2_2_2','Screen'),('3','M_2_2_3','Screen'),('4','M_2_2_4','Screen'),('5','M_2_2_5','Screen'),('6','M_2_2_6','Screen'),\
                ('r','M_2_2','Screen'),('q','Q','Screen'),('b','M_2','Screen')]

    def __init__(self):
        super().__init__()        
        self.__parent_class = 'IL_AirplaneMenu'
        self.__module = 'il_airplane_search_menu'
        self.__class_name = 'IL_AirplaneSearchMenu'