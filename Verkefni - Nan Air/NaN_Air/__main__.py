# Imports and constants
import os, sys, shutil
from InterfaceLayer.il_main_menu import IL_MainMenu
from LogicLayer.ll_api import LL_API
from ModelClasses.destination import Destination
from ModelClasses.employee import Employee
from ModelClasses.plane import Plane
from ModelClasses.trip import Trip

# Functions

def check_if_int(tuple_object):
    try:
        int(tuple_object[1])
        return int(tuple_object[1])
    except ValueError:
        return 100
    except TypeError:
        return 200

def model_class_objects():
    return (Employee(), Destination(), Plane(), Trip())

def create_employee_loop(new_screen, newEmployee):
    ''' This function performs the loop to handle creating new employees in the main program. '''
    new_screen.get_edit_funcs(newEmployee)
    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, newEmployee))
    user_input = new_screen.validate_selection(new_screen, newEmployee)
    has_input = True


def call_edit_function():
    ''' This function handles the steps needed to call a 'set' function in the main program. '''
    

def main():
    # We start by forceing the shell into a specific size.
    os.system('mode con: cols=180 lines=50')
    # Create a search objects, this allows the user to not loose his search criteria if he has to return to a previous screen.
    employeeSearchObject, destinationSearchObject, planeSearchObject, tripSearchObject = model_class_objects()
    # Create a edit object, same reasons as before.
    employeeEditObject, destinationEditObject, planeEditObject, tripEditObject = model_class_objects()
    # Create a new object, same as before. This allows the user to jump back into the same object and continue from before.
    newEmployee, newDestination, newPlane, newTrip = model_class_objects()
    current_screen = IL_MainMenu()
    print(current_screen.prep_window(current_screen.FILE,current_screen.GRAPHICS_FILE))
    user_input = current_screen.validate_selection(current_screen)
    while user_input[0] != 'q':
        has_input = False
        # Force the shell again inside the loop incase the user has resized it.
        os.system('mode con: cols=180 lines=50')        
        new_screen = current_screen.variable_class(user_input[1])
        # Delete the old screen instance to prevent functions accessing wrong data.
        del current_screen        
        if new_screen.SCREEN_TYPE == 'Create':
            if new_screen.CATEGORY == 'Employee':                
                new_screen.get_edit_funcs(newEmployee)
                print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, newEmployee))
                user_input = new_screen.validate_selection(new_screen, newEmployee)
                has_input = True
                while user_input[0][:1].lower() == 'e' or user_input[1] == 'X':
                    if user_input[0][:1].lower() == 'e':
                        method_ = getattr(newEmployee, user_input[1])
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, newEmployee))
                        input_ = input("Enter value for {}: ".format(user_input[1].replace('set_','')))                                                    
                        index = LL_API().find_employee_index(newEmployee)
                        method_(input_)
                        if index == None:
                            LL_API().new_employee(newEmployee)
                        else:
                            LL_API().edit_employee(newEmployee, index)                    
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, newEmployee))
                        user_input = new_screen.validate_selection(new_screen, newEmployee)
                    elif user_input[1] == 'X':
                        new_screen.reset_object(newEmployee)
                        list_of_objects = LL_API().search_employee(newEmployee)[:10]
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, newEmployee, list_of_objects[0:10]))
                        user_input = new_screen.validate_selection(new_screen, newEmployee, list_of_objects)
                else:
                    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, newEmployee))
        elif new_screen.SCREEN_TYPE == 'Search':
            if new_screen.CATEGORY == 'Employee':
                list_of_objects = LL_API().search_employee(employeeSearchObject)[:10]
                new_screen.get_edit_funcs(employeeSearchObject)
                new_screen.get_list_options(list_of_objects)
                new_screen.get_select_options(list_of_objects)
                print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, employeeSearchObject, list_of_objects[0:10]))
                user_input = new_screen.validate_selection(new_screen, employeeSearchObject, list_of_objects)
                has_input = True
                while user_input[0][:1].lower() == 'e' or check_if_int(user_input) < 10 or user_input[1] == 'X' or user_input[1][:1] == 's':
                    if user_input[0][:1].lower() == 'e':
                        if new_screen.SCREEN_TYPE == 'Edit':                            
                            method_ = getattr(employeeEditObject, user_input[1])
                            print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, employeeEditObject))
                            input_ = input("Enter value for {}: ".format(user_input[1].replace('set_','')))                            
                            index = LL_API().find_employee_index(employeeEditObject)
                            method_(input_)
                            LL_API().edit_employee(employeeEditObject, index)
                            print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, employeeEditObject),flush=True)
                            user_input = new_screen.validate_selection(new_screen, employeeEditObject, list_of_objects)
                        else:
                            method_ = getattr(employeeSearchObject, user_input[1])
                            list_of_objects = LL_API().search_employee(employeeSearchObject)[:10]
                            print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, employeeSearchObject, list_of_objects[0:10]))
                            input_ = input("Enter value for {}: ".format(user_input[1].replace('set_','')))
                            method_(input_)
                            list_of_objects = LL_API().search_employee(employeeSearchObject)
                            print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, employeeSearchObject, list_of_objects[0:10]))
                            user_input = new_screen.validate_selection(new_screen, employeeSearchObject, list_of_objects)
                    elif check_if_int(user_input) < 10:
                        employeeSearchObject = list_of_objects[int(user_input[1])]
                        list_of_objects = LL_API().search_employee(employeeSearchObject)[:10]
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, employeeSearchObject, list_of_objects[0:10]))
                        user_input = new_screen.validate_selection(new_screen, employeeSearchObject, list_of_objects)
                    elif user_input[1] == 'X':
                        new_screen.reset_object(employeeSearchObject)
                        list_of_objects = LL_API().search_employee(employeeSearchObject)[:10]
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, employeeSearchObject, list_of_objects[0:10]))
                        user_input = new_screen.validate_selection(new_screen, employeeSearchObject, list_of_objects)
                    elif user_input[1][:1] == 's':
                        new_screen = all_screens.employee_edit
                        employeeEditObject = list_of_objects[int(user_input[1][1:])]                        
                        new_screen.get_edit_funcs(employeeEditObject)
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, employeeEditObject))
                        user_input = new_screen.validate_selection(new_screen, employeeEditObject)                    
        else: 
            print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE))
        if not has_input:
            user_input = new_screen.validate_selection(new_screen)
        current_screen = new_screen
    else:
        new_screen = current_screen.variable_class(user_input[1])
        del current_screen
        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE))
        new_screen.single_input()

# Main program
if __name__ == '__main__':
	main()