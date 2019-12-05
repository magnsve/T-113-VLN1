# Imports and constants
from .IL_AirplaneMenu import IL_AirplaneMenu

# Classes
class IL_AirplaneCreateMenu(IL_AirplaneMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> New Airplane'
    PARENT = 'IL_AirplaneMenu'
    YOU_ARE_HERE = 'IL_AirplaneCreateMenu'    
    OPTIONS = [('1','M_2_1_1'),('2','M_2_1_2'),('3','M_2_1_3'),('4','M_2_1_4'),('5','M_2_1_5'),('r','M_2_1'),('q','Q'),('b','M_2')]