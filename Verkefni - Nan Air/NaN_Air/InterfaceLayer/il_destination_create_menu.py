# Imports and constants
from .il_destination_menu import IL_DestinationMenu
from LogicLayer.ll_api import LL_API

# Classes
class IL_DestinationCreateMenu(IL_DestinationMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/DestinationCreateMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/DestinationCreate_graphics.txt'
    ADDRESS = 'Main Menu -> Destinations -> New Destination'
    SCREEN_TYPE = 'Create'
    CATEGORY = 'Destination' 
    OPTIONS = [('1','M_3_1_1'),('2','M_3_1_2'),('r','M_3_1'),('q','Q'),('b','M_3')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_DestinationMenu'
        self.__module = 'il_destination_create_menu'
        self.__class_name = 'IL_DestinationCreateMenu'
    
    def display_model_object(self, destination_object = None):        
        if destination_object:            
            ssn = '1 - SSN: {}'.format(destination_object.get_ssn())
            name = '2 - Name: {}'.format(destination_object.get_name())
            role = '3 - Role: {}'.format(destination_object.get_role())
            rank = '4 - Rank: {}'.format(destination_object.get_rank())
            licence = '5 - Licence: {}'.format(destination_object.get_licence())
            address = '6 - Address: {}'.format(destination_object.get_address())
            phonenumber = '7 - Phonenumber: {}'.format(destination_object.get_phonenumber())
            status = '8 - Status: {}'.format(destination_object.get_status())
            return [ssn, name, role, rank, licence, address, phonenumber, status]
        else:
            return ''