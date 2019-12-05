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
    MENUS = {'M': 'IL_MainMenu', \
            'M_1': 'IL_EmployeeMenu', \
            'M_1_1':'IL_EmployeeCreateMenu', \
            'M_1_2': 'IL_EmployeeSearchMenu',\
            'M_2': 'IL_AirplaneMenu', \
            'M_2_1': 'IL_AirplaneCreateMenu', \
            'M_2_2': 'IL_AirplaneSearchMenu', \
            'M_3': 'IL_DestinationMenu', \
            'M_3_1': 'IL_DestinationCreateMenu', \
            'M_3_2': 'IL_DestinationSearchMenu', \
            'M_4': 'IL_TripsMenu', \
            'M_4_1': 'IL_TripsCreateMenu',\
            'M_4_2': 'IL_TripsSearchMenu',\
            'Q':'IL_QuitScreen'}