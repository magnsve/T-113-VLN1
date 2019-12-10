# Imports and constants
from .il_printer import IL_Printer

# Classes
class IL_MainMenu(IL_Printer):
    ''' '''
    
    FILE = 'InterfaceLayer/UI_MetaData/MainMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/MainMenu_graphics.txt'
    ADDRESS = 'Main Menu'
    SCREEN_TYPE = 'Menu'
    CATEGORY = 'Main' 
    OPTIONS = [('1','M_1','Screen'),('2','M_2','Screen'),('3','M_3','Screen'),('4','M_4','Screen'),('r','M','Screen'),('q','Q','Screen'),('b','M','Screen')]

    def __init__(self):        
        super().__init__()
        self.__parent_class = 'IL_MainMenu'
        self.__module = 'il_main_menu'
        self.__class_name = 'IL_MainMenu'        