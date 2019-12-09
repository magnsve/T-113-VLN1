# Imports and constants
from .il_airplane_menu import IL_AirplaneMenu

# Classes
class IL_AirplaneCreateMenu(IL_AirplaneMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> New Airplane'
    SCREEN_TYPE = 'Create'
    CATEGORY = 'Planes' 
    OPTIONS = [ ('1','M_2_1_1','Screen'),('2','M_2_1_2','Screen'),('3','M_2_1_3','Screen'),('4','M_2_1_4','Screen'),('5','M_2_1_5','Screen'),\
                ('r','M_2_1','Screen'),('q','Q','Screen'),('b','M_2','Screen')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_AirplaneMenu'
        self.__module = 'il_airplane_create_menu'
        self.__class_name = 'IL_AirplaneCreateMenu'