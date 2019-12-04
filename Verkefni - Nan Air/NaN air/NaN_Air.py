# Imports
import os
from InterfaceLayer.Interface import IL_MainMenu

# Functions
def main():
    os.system('mode con: cols=150 lines=40')
    current_pos = IL_MainMenu()    
    current_pos.print_window(current_pos.FILE,current_pos.GRAPHICS_FILE)    
    user_input = current_pos.validate_selection()        
    while user_input != 'q':
        new_pos = current_pos.variable_class(user_input[1])
        cleanup = current_pos.YOU_ARE_HERE
        del cleanup        
        os.system('mode con: cols=150 lines=40')
        new_pos.print_window(new_pos.FILE,new_pos.GRAPHICS_FILE)
        user_input = new_pos.validate_selection()
        current_pos = new_pos
    else:
        current_pos.quitscreen()

# Main program
if __name__ == '__main__':
	main()