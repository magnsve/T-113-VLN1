# Imports and constants
from .il_printer import IL_Printer
from LogicLayer.ll_api import LL_API

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
    
    def list_of_get_functions(self, model_class_object):
        return [func for func in dir(model_class_object) if callable(getattr(model_class_object, func)) and func.startswith("get")]
    
    def list_of_set_functions(self, model_class_object):
        return [func for func in dir(model_class_object) if callable(getattr(model_class_object, func)) and func.startswith("set")]
    
    def get_edit_funcs(self, model_class_object):
        options_list = []
        options = self.list_of_set_functions(model_class_object)
        for index, item in enumerate(options):
            options_list.append(('e' + str(index + 1), item,'Func'))
        for item in options_list:
            self.OPTIONS.append(item)
    
    def get_list_options(self, list_of_objects):
        options_list = []        
        for i in range(len(list_of_objects[:10])):
            options_list.append((str(i+1),str(i),'Lists'))
        for item in options_list:
            self.OPTIONS.append(item)        

    def display_search_object(self, model_class_object = None):
        output = ''
        method_ = getattr(LL_API(), "get_"+self.CATEGORY.lower()+"_header")
        header_row = method_()
        header_row.sort()
        item_values = model_class_object.__dict__
        sorted(item_values)
        column_width = 40
        counter = 0
        for index, item in enumerate(header_row):
            output += 'E{} {}: {}'.format(index+1,item.upper(),item_values['_'+self.CATEGORY+"__"+item]).ljust(column_width)
            counter += 1
            if counter == 3:
                output += '\n'
                counter = 0
        return output
    
    def search_model_object(self, list_of_objects = None):
        method_ = getattr(LL_API(), "get_"+self.CATEGORY.lower()+"_header")
        header_row = method_()        
        column_width = 130 // (len(header_row)+1)
        output = 'No'.center(column_width)
        for item in header_row:
            output += item.upper().ljust(column_width)
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
        output += '\n'
        output += 'Search returned {} results.\n'.format(len(list_of_objects)).center(130)
        return output