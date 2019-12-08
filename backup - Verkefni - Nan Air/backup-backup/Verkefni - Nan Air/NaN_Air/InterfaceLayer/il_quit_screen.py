# Imports and constants
from .il_main_menu import IL_MainMenu

# Classes
class IL_QuitScreen(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/QuitScreen.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/QuitScreen_graphics.txt'    
    FACTS = 'InterfaceLayer/UI_MetaData/FactsAboutOurFounder.txt'
    SCREEN_TYPE = 'Menu'
    CATEGORY = 'Quit'

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_MainMenu'
        self.__module = 'il_quit_screen'
        self.__class_name = 'IL_QuitScreen'