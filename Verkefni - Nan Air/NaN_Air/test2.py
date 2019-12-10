# Imports and constants
import os, sys
from InterfaceLayer.il_screens import Screens
from LogicLayer.ll_api import LL_API
from ModelClasses.destination import Destination
from ModelClasses.employee import Employee
from ModelClasses.plane import Plane
from ModelClasses.trip import Trip

def main():
    os.system('mode con: cols=200 lines=40')
    all_screens = Screens()
    main_menu = all_screens.main_menu
    print(main_menu.prep_window(main_menu.FILE,main_menu.GRAPHICS_FILE))
    _input = input("Enter your selection: ")
    if _input == '1':
        employees = all_screens.employee
        print(employees.prep_window(employees.FILE,employees.GRAPHICS_FILE))
        _input = input("Enter your selection: ")
        if _input == '1':
            employee = Employee()
            new_employee = all_screens.employee_create
            print(new_employee.prep_window(new_employee.FILE,new_employee.GRAPHICS_FILE, employee))
            _input = input("Enter your selection: ")

# Main program
main()