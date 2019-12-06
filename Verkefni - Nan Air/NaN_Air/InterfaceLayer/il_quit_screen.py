# Imports and constants
from .il_main_menu import IL_MainMenu

# Classes
class IL_QuitScreen(IL_MainMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/QuitScreen.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/QuitScreen_graphics.txt'    
    PARENT = 'IL_MainMenu'
    YOU_ARE_HERE = 'IL_QuitScreen'
    FACTS = 'InterfaceLayer/UI_MetaData/FactsAboutOurFounder.txt'