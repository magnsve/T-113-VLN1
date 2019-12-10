# Imports and constants
from .il_employee_search_menu import IL_EmployeeSearchMenu
from LogicLayer.ll_api import LL_API

# Classes
class IL_EmployeeEditMenu(IL_EmployeeSearchMenu):
    ''' '''
    FILE = 'InterfaceLayer/UI_MetaData/EmployeeEditMenu.txt'
    GRAPHICS_FILE = 'InterfaceLayer/UI_MetaData/EmployeeEdit_graphics.txt'
    ADDRESS = 'Main Menu -> Employees -> Find Employee -> Edit Employee'
    SCREEN_TYPE = 'Edit'
    CATEGORY = 'Employee'
    OPTIONS = [('r','M_1_2_1','Screen'),('q','Q','Screen'),('b','M_1_2','Screen'),('x','X','Reset')]

    def __init__(self):
        super().__init__()
        self.__parent_class = 'IL_EmployeeSearchMenu'
        self.__module = 'il_employee_edit_menu'
        self.__class_name = 'IL_EmployeeEditMenu'