# Imports
import os, sys
from InterfaceLayer.il_main_menu import IL_MainMenu
from LogicLayer.ll_api import LL_API
from ModelClasses.destination import Destination
from ModelClasses.employee import Employee
from ModelClasses.plane import Plane
from ModelClasses.trip import Trip

# Functions
def main():
    os.system('mode con: cols=150 lines=40')    
    current_pos = IL_MainMenu()    
    print(current_pos.prep_window(current_pos.FILE,current_pos.GRAPHICS_FILE))
    user_input = current_pos.validate_selection(current_pos)
    while user_input[0] != 'q':
        os.system('mode con: cols=150 lines=40')
        new_pos = current_pos.variable_class(user_input[1])
        del current_pos
        if new_pos.SCREEN_TYPE == 'Create':
            if new_pos.CATEGORY == 'Employee':
                model_class_object = Employee()
                print(new_pos.prep_window(new_pos.FILE,new_pos.GRAPHICS_FILE, model_class_object))
        elif new_pos.SCREEN_TYPE == 'Search':
            if new_pos.CATEGORY == 'Employee':
                model_class_object = Employee()
                list_of_objects = LL_API().search_employee(model_class_object)
                if len(list_of_objects) > 10:
                    print(new_pos.prep_window(new_pos.FILE,new_pos.GRAPHICS_FILE, list_of_objects[0:10]))
                else:
                    print(new_pos.prep_window(new_pos.FILE,new_pos.GRAPHICS_FILE, list_of_objects))
        else: 
            print(new_pos.prep_window(new_pos.FILE,new_pos.GRAPHICS_FILE))
        user_input = new_pos.validate_selection(new_pos)
        current_pos = new_pos
    else:
        new_pos = current_pos.variable_class(user_input[1])
        del current_pos
        print(new_pos.prep_window(new_pos.FILE,new_pos.GRAPHICS_FILE))
        new_pos.single_input()

# Main program
if __name__ == '__main__':
	main()