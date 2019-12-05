# Imports and constants
from .IL_AirplaneMenu import IL_AirplaneMenu

# Classes
class IL_AirplaneSearchMenu(IL_AirplaneMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/AirplaneSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/AirplaneSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Airplanes -> Find Airplane'
    PARENT = 'IL_AirplaneMenu'
    YOU_ARE_HERE = 'IL_AirplaneSearchMenu'    
    OPTIONS = [('1','M_2_2_1'),('2','M_2_2_2'),('3','M_2_2_3'),('4','M_2_2_4'),('5','M_2_2_5'),('6','M_2_2_6'),('r','M_2_2'),('q','Q'),('b','M_2')]