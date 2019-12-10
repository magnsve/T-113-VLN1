# Imports and constants
import os, sys, shutil
from InterfaceLayer.il_screens import Screens
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
        return

def model_class_objects():
    return (Employee(), Destination(), Plane(), Trip())

def main():
    # We start by forcing the shell to predefined size.
    os.system('mode con: cols=180 lines=50')
    # We create an instance of all model classes that are dedicated for searching. This allows the user to go back to a previous screen and stil have the data he was working on.
    employeeSearchObject, destinationSearchObject, planeSearchObject, tripSearchObject = model_class_objects()
    # Same here, only for editing entries.
    employeeEditObject, destinationEditObject, planeEditObject, tripEditObject = model_class_objects()
    # And again, now for creating new entries into the database.
    newEmployee, newDestination, newPlane, newTrip = model_class_objects()    
    all_screens = Screens()
    current_screen = all_screens.main_menu
    print(current_screen.prep_window(current_screen.FILE,current_screen.GRAPHICS_FILE))
    user_input = current_screen.validate_selection(current_screen)
    while user_input[0] != 'q':
        has_input = False
        # We force the shell again to resize it if the user has changed the size since the screen was last drawn.
        os.system('mode con: cols=180 lines=50')
        new_screen = current_screen.variable_class(user_input[1])
        del current_screen
        # By using the SCREEN_TYPE arguments we can identify what the user wants to do.
        if new_screen.SCREEN_TYPE == 'Create':
            if new_screen.CATEGORY == 'Employee':
                new_object = newEmployee
            elif new_screen.CATEGORY == 'Destination':
                new_object = newDestination
            elif new_screen.CATEGORY == 'Planes':
                new_object = newPlane
            elif new_screen.CATEGORY == 'Trips':
                new_object = newTrip
            # This function delves into the new_screen class instancee and adds valid options to it based on what 'set' functions are in the new_object model class instance. 
            # This allows the input validation function to correctly identify valid vs. invalid input.
            new_screen.get_edit_funcs(new_object)
            print(new_screen.prep_window(new_screen.FILE, new_screen.GRAPHICS_FILE, new_object))
            user_input = new_screen.validate_selection(new_screen, new_object)
            has_input = True
            while user_input[0][:1].lower() == 'e' or user_input[1] == 'X':
                if user_input[0][:1].lower() == 'e':
                    # Using getattr gives us the option to dynamically call the desired function instead of having to create the site map.
                    method_ = getattr(new_object, user_input[1])
                    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, new_object))
                    input_ = input("Enter value for {}: ".format(user_input[1].replace('set_','')))
                    # Here we find the index of the file in the database.
                    index_func = getattr(LL_API(), "find_"+new_screen.CATEGORY.lower()+"_index")
                    index = index_func(new_object)                    
                    method_(input_)
                    # If the object is not found in the database the index is returned as 'None'. We then append the new object to the database instead of overwrite it.
                    if index == None:
                        new_func = getattr(LL_API(), "new_"+new_screen.CATEGORY.lower())
                        new_func(new_object)
                    else:
                        edit_func = getattr(LL_API(), "edit_"+new_screen.CATEGORY.lower())
                        edit_func(new_object, index)
                    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, new_object))
                    user_input = new_screen.validate_selection(new_screen, new_object)
                # Option for resetting the object, i.e. when the user wants to start a new entry.
                elif user_input[1] == 'X':
                    new_screen.reset_object(new_object)
                    search_func = getattr(LL_API(), "search_"+new_screen.CATEGORY.lower())
                    list_of_objects = search_func(new_object)[:10]                    
                    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, new_object, list_of_objects[0:10]))
                    user_input = new_screen.validate_selection(new_screen, new_object, list_of_objects)
            else:
                print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, new_object))                        
        elif new_screen.SCREEN_TYPE == 'Search':
            if new_screen.CATEGORY == 'Employee':
                search_object = employeeSearchObject
                edit_object = employeeEditObject
            elif new_screen.CATEGORY == 'Destination':
                search_object = destinationSearchObject
                edit_object = destinationEditObject
            elif new_screen.CATEGORY == 'Planes':
                search_object = planeSearchObject
                edit_object = planeEditObject
            elif new_screen.CATEGORY == 'Trips':
                search_object = tripSearchObject
                edit_object = tripEditObject
            search_func = getattr(LL_API(), "search_"+new_screen.CATEGORY.lower())
            list_of_objects = search_func(search_object)[:10]
            # Here we add options to the new_screen instance to allow for 'set' functions, to set an object from the search results as the current search parameters 
            # and to select an item from the list to open in an edit window.
            new_screen.get_edit_funcs(search_object)
            new_screen.get_list_options(list_of_objects)
            new_screen.get_select_options(list_of_objects)
            print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, search_object, list_of_objects[0:10]))
            user_input = new_screen.validate_selection(new_screen, search_object, list_of_objects)
            has_input = True
            while user_input[0][:1].lower() == 'e' or check_if_int(user_input) < 10 or user_input[1] == 'X' or user_input[1][:1] == 's':
                if user_input[0][:1].lower() == 'e':
                    if new_screen.SCREEN_TYPE == 'Edit':
                        method_ = getattr(edit_object, user_input[1])
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, edit_object))
                        input_ = input("Enter value for {}: ".format(user_input[1].replace('set_','')))                                                    
                        index_func = getattr(LL_API(), "find_"+new_screen.CATEGORY.lower()+"_index")
                        index = index_func(edit_object)
                        method_(input_)
                        edit_func = getattr(LL_API(), "edit_"+new_screen.CATEGORY.lower())
                        edit_func(new_object, index)                        
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, edit_object))
                        user_input = new_screen.validate_selection(new_screen, edit_object, list_of_objects)
                    else:
                        method_ = getattr(search_object, user_input[1])
                        search_func = getattr(LL_API(), "search_"+new_screen.CATEGORY.lower())
                        list_of_objects = search_func(search_object)[:10]
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, search_object, list_of_objects[0:10]))
                        input_ = input("Enter value for {}: ".format(user_input[1].replace('set_','')))
                        method_(input_)
                        list_of_objects = search_func(search_object)[:10]
                        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, search_object, list_of_objects[0:10]))
                        user_input = new_screen.validate_selection(new_screen, search_object, list_of_objects)
                # This check is to determine if the user entered an intager.
                elif check_if_int(user_input) < 10:
                    search_object = list_of_objects[int(user_input[1])]
                    search_func = getattr(LL_API(), "search_"+new_screen.CATEGORY.lower())
                    list_of_objects = search_func(search_object)[:10]
                    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, search_object, list_of_objects[0:10]))
                    user_input = new_screen.validate_selection(new_screen, search_object, list_of_objects)
                elif user_input[1] == 'X':
                    new_screen.reset_object(search_object)
                    search_func = getattr(LL_API(), "search_"+new_screen.CATEGORY.lower())
                    list_of_objects = search_func(search_object)[:10]                    
                    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, search_object, list_of_objects[0:10]))
                    user_input = new_screen.validate_selection(new_screen, search_object, list_of_objects)
                # Here we select an object from the list and open it in an edit screen.
                elif user_input[1][:1] == 's':
                    go_to_edit = getattr(all_screens, new_screen.CATEGORY.lower()+'_edit')
                    new_screen = go_to_edit
                    edit_object = list_of_objects[int(user_input[1][1:])]                        
                    new_screen.get_edit_funcs(edit_object)
                    print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE, edit_object))
                    user_input = new_screen.validate_selection(new_screen, edit_object)                    
        else:
            print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE))
        if not has_input:
            user_input = new_screen.validate_selection(new_screen)
        current_screen = new_screen
    else:
        # Quitscreen
        new_screen = current_screen.variable_class(user_input[1])
        del current_screen
        print(new_screen.prep_window(new_screen.FILE,new_screen.GRAPHICS_FILE))
        new_screen.single_input()        

# Main program
if __name__ == '__main__':
	main()