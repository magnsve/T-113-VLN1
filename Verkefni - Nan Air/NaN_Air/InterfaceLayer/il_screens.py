from .il_airplane_create_menu import IL_AirplaneCreateMenu
from .il_airplane_menu import IL_AirplaneMenu
from .il_airplane_search_menu import IL_AirplaneSearchMenu
from .il_airplane_edit_menu import IL_AirplaneEditMenu
from .il_airplane_list_menu import IL_AirplaneListMenu
from .il_employee_menu import IL_EmployeeMenu
from .il_employee_create_menu import IL_EmployeeCreateMenu
from .il_employee_search_menu import IL_EmployeeSearchMenu
from .il_employee_edit_menu import IL_EmployeeEditMenu
from .il_employee_list_menu import IL_EmployeeListMenu
from .il_trips_menu import IL_TripsMenu
from .il_trips_create_menu import IL_TripsCreateMenu
from .il_trips_search_menu import IL_TripsSearchMenu
from .il_trips_edit_menu import IL_TripsEditMenu
from .il_trips_list_menu import IL_TripsListMenu
from .il_destination_menu import IL_DestinationMenu
from .il_destination_create_menu import IL_DestinationCreateMenu
from .il_destination_search_menu import IL_DestinationSearchMenu
from .il_destination_edit_menu import IL_DestinationEditMenu
from .il_destination_list_menu import IL_DestinationListMenu
from .il_main_menu import IL_MainMenu

class Screens():
    ''' Creates an instance of all Interface Layer classes to use in the main program. '''
    def __init__(self):
        self.plane_create = IL_AirplaneCreateMenu()
        self.plane = IL_AirplaneMenu()
        self.plane_search = IL_AirplaneSearchMenu()
        self.plane_edit = IL_AirplaneEditMenu()
        self.plane_list = IL_AirplaneListMenu()
        self.employee = IL_EmployeeMenu()
        self.employee_create = IL_EmployeeCreateMenu()
        self.employee_search = IL_EmployeeSearchMenu()
        self.employee_edit = IL_EmployeeEditMenu()
        self.employee_list = IL_EmployeeListMenu()
        self.trip = IL_TripsMenu()
        self.trip_create = IL_TripsCreateMenu()
        self.trip_search = IL_TripsSearchMenu()
        self.trip_edit = IL_TripsEditMenu()
        self.trip_list = IL_TripsListMenu()
        self.destination = IL_DestinationMenu()
        self.destination_create = IL_DestinationCreateMenu()
        self.destination_search = IL_DestinationSearchMenu()
        self.destination_edit = IL_DestinationEditMenu()
        self.destination_list = IL_DestinationListMenu()
        self.main_menu = IL_MainMenu()
        