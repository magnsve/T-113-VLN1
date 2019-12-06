# Imports and constants
from .il_airplane_menu import IL_AirplaneMenu

# Classes
class IL_AirplaneCreateMenu(IL_AirplaneMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> New Airplane'
    OPTIONS = [('1','M_2_1_1'),('2','M_2_1_2'),('3','M_2_1_3'),('4','M_2_1_4'),('5','M_2_1_5'),('r','M_2_1'),('q','Q'),('b','M_2')]

    def __init__(self):
        self.__parent_class = 'IL_AirplaneMenu'
        self.__module = 'il_airplane_create_menu'
        self.__class_name = 'IL_AirplaneCreateMenu'
        super().__init__()