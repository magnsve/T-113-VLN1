# Imports and constants
from .il_printer import IL_Printer

# Classes
class IL_MainMenu(IL_Printer):
    ''' '''
    
    FILE = 'InterfaceLayer/UI_MetaData/MainMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/MainMenu_graphics.txt'
    ADDRESS = 'Main Menu'
    OPTIONS = [('1','M_1'),('2','M_2'),('3','M_3'),('4','M_4'),('r','M'),('q','Q'),('b','M')]

    def __init__(self):        
        self.__parent_class = 'IL_MainMenu'
        self.__module = 'il_main_menu'
        self.__class_name = 'IL_MainMenu'
        self.__screen_type = 'Menu'
        self.__category = 'Main'
        super().__init__()
    
    def get_screen_type(self):
        return self.__screen_type
    
    def get_category(self):
        return self.__category