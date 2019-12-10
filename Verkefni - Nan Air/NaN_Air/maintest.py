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

def create_loop(new_screen, newObject):
    ''' This function performs the loop to handle creating new employees in the main program. '''
    new_screen.get_edit_funcs(newObject)
    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, newObject))
    user_input = new_screen.validate_selection(new_screen, newObject)    
    while user_input[0][:1].lower() == 'e' or user_input[1] == 'X':
        if user_input[0][:1].lower() == 'e':
            user_input = call_edit_function(newObject, user_input, new_screen)
        else:
            newObject = call_reset_function(new_screen, newObject)
    else:
        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, newObject))
    return ()

def call_reset_function(new_screen, newObject):
    ''' This function handles the reset function. '''
    new_screen.reset_object(newObject)
    list_of_objects = LL_API().search_employee(newObject)[:10]
    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, newObject, list_of_objects[0:10]))
    user_input = new_screen.validate_selection(new_screen, newObject, list_of_objects)

def call_edit_function(model_object, user_input, new_screen):
    ''' This function handles the steps needed to call a 'set' function in the main program. '''
    method_ = getattr(model_object, user_input[1])
    if new_screen.CATEGORY == 'Edit':        
        if new_screen.SCREEN_TYPE == 'Employee':
            index = LL_API().find_employee_index(model_object)
        elif new_screen.SCREEN_TYPE == 'Destination':
            index = LL_API().find_destination_index(model_object)
        elif new_screen.SCREEN_TYPE == 'Planes':
            index = LL_API().find_plane_index(model_object)
        else:
            index = ll_api().find_trip_index(model_object)
        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, model_object))
    else:
        if new_screen.SCREEN_TYPE == 'Employee':
            list_of_objects = LL_API().search_employee(model_object)[:10]
        elif new_screen.SCREEN_TYPE == 'Destination':
            list_of_objects = LL_API().search_destination(model_object)[:10]
        elif new_screen.SCREEN_TYPE == 'Plane':
            list_of_objects = LL_API().search_plane(model_object)[:10]
        else:
            list_of_objects = LL_API().search_trip(model_object)[:10]
        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, model_object, list_of_objects[0:10]))    
    input_ = input("Enter value for {}: ".format(user_input[1].replace('set_','')))
    method_(input_)
    if new_screen.CATEGORY != 'Search':
        if index == None:
            if new_screen.CATEGORY == 'Employee':
                LL_API().new_employee(model_class_object)
            '''elif new_screen.CATEGORY == 'Destination':
                LL_API().new_destination(model_class_object)
            elif new_screen.CATEGORY == 'Planes':
                LL_API().new_plane(model_class_object)
            else: 
                LL_API().new_trip(model_class_object)'''
        else:
            if new_screen.CATEGORY == 'Employee':
                LL_API().edit_employee(model_class_object, index)
            '''elif new_screen.CATEGORY == 'Destination':
                LL_API().edit_destination(model_class_object)
            elif new_screen.CATEGORY == 'Planes':
                LL_API().edit_plane(model_class_object)
            else: 
                LL_API().edit_trip(model_class_object)        '''
    if new_screen.CATEGORY == 'Search':
        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, model_object, list_of_objects[0:10]))        
    else:
        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, model_object))
    user_input = new_screen.validate_selection(new_screen, employeeEditObject, list_of_objects)
    return (model_object, user_input, new_screen)


def search_loop(new_screen, model_object):
    if new_screen.CATEGORY == 'Employee':
        list_of_objects = LL_API().search_employee(model_object)[:10]
    elif new_screen.CATEGORY == 'Destination':
        list_of_objects = LL_API().search_destination(model_object)[:10]
    elif new_screen.CATEGORY == 'Planes':
        list_of_objects = LL_API().search_plane(model_object)[:10]
    else: 
        list_of_objects = LL_API().search_trip(model_object)[:10]        
    # Adding options for 'set' functions, for being able to set search parameters to an object from a list and for being able to 
    # select and item from the list and go to an edit screen.
    new_screen.get_edit_funcs(model_object)
    new_screen.get_list_options(list_of_objects)
    new_screen.get_select_options(list_of_objects)
    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, model_object, list_of_objects[0:10]))
    user_input = new_screen.validate_selection(new_screen, model_object, list_of_objects)
    while user_input[0][:1].lower() == 'e' or check_if_int(user_input) < 10 or user_input[1] == 'X' or user_input[1][:1] == 's':
        if user_input[0][:1].lower() == 'e':
            call_edit_function(edit_object, user_input, new_screen)
        elif check_if_int(user_input) < 10:
            model_object = list_of_objects[int(user_input[1])]
            list_of_objects = LL_API().search_employee(model_object)[:10]
            print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, model_object, list_of_objects[0:10]))
            user_input = new_screen.validate_selection(new_screen, model_object, list_of_objects)
        elif user_input[1] == 'X':
            call_reset_function(new_screen, model_object)
        elif user_input[1][:1] == 's':                    
            choose_from_list(new_screen, model_object, list_of_objects)
            
def choose_from_list(new_screen, model_object, list_of_objects):
    if new_screen.CATEGORY == 'Employee':
        new_screen = all_screens.employee_edit
    elif new_screen.CATEGORY == 'Destination':
        new_screen = all_screens.destination_edit
    elif new_screen.CATEGORY == 'Planes':
        new_screen = all_screens.plane_edit
    else:
        new_screen = all_screens.trip_edit
    model_object = list_of_objects[int(user_input[1][1:])]
    new_screen.get_edit_funcs(model_object)
    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, model_object))
    user_input = new_screen.validate_selection(new_screen, model_object)
    return 
                        
                        


#def call_selection_options()

def main():
    # We start by forceing the shell into a specific size.
    os.system('mode con: cols=180 lines=50')
    # Create a search objects, this allows the user to not loose his search criteria if he has to return to a previous screen.
    employeeSearchObject = model_class_objects()[1]
    # employeeSearchObject, destinationSearchObject, planeSearchObject, tripSearchObject = model_class_objects()
    # Create a edit object, same reasons as before.
    employeeEditObject = model_class_objects()[1]
    # employeeEditObject, destinationEditObject, planeEditObject, tripEditObject = model_class_objects()
    # Create a new object, same as before. This allows the user to jump back into the same object and continue from before.
    newEmployee = model_class_objects()[1]
    #newEmployee, newDestination, newPlane, newTrip = model_class_objects()
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
            has_input = True
            create_loop(new_screen, newEmployee)
        elif new_screen.SCREEN_TYPE == 'Search':
            has_input = True
            search_loop(new_screen, employeeSearchObject):


# Main program
if __name__ == '__main__':
	main()