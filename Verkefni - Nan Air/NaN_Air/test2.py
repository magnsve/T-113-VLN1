# Imports and constants
import os, sys
from InterfaceLayer.il_main_menu import IL_MainMenu
from LogicLayer.ll_api import LL_API
from ModelClasses.destination import Destination
from ModelClasses.employee import Employee
from ModelClasses.plane import Plane
from ModelClasses.trip import Trip

def check_if_int(tuple_object):
    try:
        int(tuple_object[1])
        return int(tuple_object[1])
    except ValueError:
        return 100
    except TypeError:
        return 200

# Functions
def main():    
    os.system('mode con: cols=150 lines=40')    
    current_pos = IL_MainMenu()    
    print(current_pos.prep_window(current_pos.FILE,current_pos.GRAPHICS_FILE))
    user_input = current_pos.validate_selection(current_pos)
    if user_input[2] == 'Screen':
        has user_input = False
        os.system('mode con: cols=150 lines=40')
        new_pos = current_pos.variable_class(user_input[1])
        del current_pos


# Main program
if __name__ == '__main__':
	main()