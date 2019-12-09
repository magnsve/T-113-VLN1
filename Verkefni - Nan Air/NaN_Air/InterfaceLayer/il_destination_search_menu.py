# Imports and constants
from .il_destination_menu import IL_DestinationMenu
from LogicLayer.ll_api import LL_API

# Classes
class IL_DestinationSearchMenu(IL_DestinationMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationSearchMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationSearch_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> Find Destination'
    SCREEN_TYPE = 'Search'
    CATEGORY = 'Destination'
    OPTIONS = [('1','M_3_2_1','Screen'),('2','M_3_2_1','Screen'),('r','M_3_2','Screen'),('q','Q','Screen'),('b','M_3','Screen')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_DestinationMenu'
        self.__module = 'il_destination_search_menu'
        self.__class_name = 'IL_DestinationSearchMenu'
    
    def search_model_object(self, list_of_objects = None):
        header_row = LL_API().get_destination_header()
        column_width = 130 // (len(header_row)+1)
        output = 'No'.center(column_width)
        for item in header_row:
            output += item.capitalize().ljust(column_width)
        output += '{}{}{}'.format('\n','-'*130,'\n')
        for index, item in enumerate(list_of_objects):
            item_values = item.__dict__.values()            
            string = '{}'.format(index+1).center(column_width)
            for element in item_values:
                if len(element) > (column_width - 1):
                    string += (element[0:(column_width-5)] + '...').ljust(column_width)
                else:
                    string += element.ljust(column_width)
            output += string + '\n'        
        return output