# This file contains constants that are used in the interface layer.

class IL_Constants():
    ''' '''
    CROSS = '+'
    VERTICAL = '|'
    HORIZONTAL = '-'
    SPACE = ' '
    SEPERATOR = '--sep--'
    GRAPHICS = '--gra--'
    CENTER_JUST = '--cen--'
    RIGHT_JUST = '--rju--'
    INDENT = '--ind--'
    LEFT_JUST = '--lju--'
    SPACING = '--spa--'
    EMPTY_LINE = '--emp--'
    BREAD_CRUMBS = '--bre--'
    SECOND_INDENT = '--sec--'
    FACTS = '--fact--'
    MENUS = {'M': ('il_main_menu','IL_MainMenu'), \
            'M_1': ('il_employee_menu','IL_EmployeeMenu'), \
            'M_1_1': ('il_employee_create_menu','IL_EmployeeCreateMenu'), \
            'M_1_2': ('il_employee_search_menu','IL_EmployeeSearchMenu'),\
            'M_2': ('il_airplane_menu','IL_AirplaneMenu'), \
            'M_2_1': ('il_airplane_create_menu','IL_AirplaneCreateMenu'), \
            'M_2_2': ('il_airplane_search_menu','IL_AirplaneSearchMenu'), \
            'M_3': ('il_destination_menu','IL_DestinationMenu'), \
            'M_3_1': ('il_destination_create_menu','IL_DestinationCreateMenu'), \
            'M_3_2': ('il_destination_search_menu','IL_DestinationSearchMenu'), \
            'M_4': ('il_trips_menu','IL_TripsMenu'), \
            'M_4_1': ('il_trips_create_menu','IL_TripsCreateMenu'),\
            'M_4_2': ('il_trips_search_menu','IL_TripsSearchMenu'),\
            'Q':('il_quit_screen','IL_QuitScreen')}    