import datetime
import dateutil.parser
from DataLayer.dl_api import DL_API
from ModelClasses.trip import Trip

class LL_Trips():
    
    def search_trips(self, trip_object):
        # okkur vantar fleiri upplýsingar hér
        list_of_trips = DL_API().get_trips
        destination_search = self.search_destination(trip_object, list_of_trips)
        plane_search = self.search_plane(trip_object, destination_search)        
        captain_search = self.search_pilot(trip_object, plane_search)
        copilot_search = self.search_copilot(trip_object, captain_search)
        cabincrew_search = self.search_cabincrew(trip_object, copilot_search)
        availableSeats_search = self.search_availableSeats(trip_object, cabincrew_search)
        outDep_search = self.search_out_dep(trip_object, availableSeats_search)
        inDep_search = self.search_in_dep(trip_object, outDep_search)
        capacity_search = self.search_capacity(trip_object, inDep_search)
        flightNr_search = self.search_flightNr(trip_object, capacity_search)
        fsm_search = self.search_fsm(trip_object, flightNr_search)
        fa1_search = self.search_fa1(trip_object, fsm_search)
        fa2_search = self.search_fa2(trip_object, fa1_search)
        fa3_search = self.search_fa3(trip_object, fa2_search)
        fa4_search = self.search_fa4(trip_object, fa3_search)
        fa5_search = self.search_fa5(trip_object, fa4_search)

        status_search = self.search_status(trip_object, flightNr_search)
        return status_search

    def search_destination(self, trip_object, list_of_trips):
        destination = trip_object.get_destination()
        output = []
        if not destination:
            return list_of_trips
        elif destination != '':
            for trip in list_of_trips:
                if destination.lower() in trip.get_destination().lower():
                    output.append(destination)
            return output
        else:
            return list_of_trips

    def search_plane(self, trip_object, list_of_trips):
        plane = trip_object.get_plane()
        output = []
        if not plane:
            return list_of_trips
        elif plane != '':
            for trip in list_of_trips:
                if plane.lower() in trip.get_plane().lower():
                    output.append(plane)
            return output
        else:
            return list_of_trips

    def search_captain(self, trip_object, list_of_trips):
        captain = trip_object.get_captain()
        output = []
        if not captain:
            return list_of_trips
        elif captain != '':
            for trip in list_of_trips:
                if captain.lower() in trip.get_captain().lower():
                    output.append(captain)
            return output
        else:
            return list_of_trips

    def search_cabincrew(self, trip_object, list_of_trips):
        cabincrew = trip_object.get_cabincrew()
        output = []
        if not cabincrew:
            return list_of_trips
        elif cabincrew != '':
            for trip in list_of_trips:
                if cabincrew.lower() in trip.get_cabincrew().lower():
                    output.append(cabincrew)
            return output
        else:
            return list_of_trips

    def search_sold_seats(self, trip_object, list_of_trips):
        sold_seats = trip_object.get_sold_seats()
        output = []
        if not sold_seats:
            return list_of_trips
        elif sold_seats != '':
            for trip in list_of_trips:
                if sold_seats.lower() in trip.get_sold_seats().lower():
                    output.append(sold_seats)
            return output
        else:
            return list_of_trips

    def search_available_seats(self, trip_object, list_of_trips):
        available_seats = trip_object.get_available_seats()
        output = []
        if not available_seats:
            return list_of_trips
        elif available_seats != '':
            for trip in list_of_trips:
                if available_seats.lower() in trip.get_available_seats().lower():
                    output.append(available_seats)
            return output
        else:
            return list_of_trips

    def search_first_trip(self, trip_object, list_of_trips):
        first_trip = trip_object.get_first_trip()
        output = []
        if not first_trip:
            return list_of_trips
        elif first_trip != '':
            for trip in list_of_trips:
                if first_trip.lower() in trip.get_first_trip().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    def search_second_trip(self, trip_object, list_of_trips):
        second_trip = trip_object.get_second_trip()
        output = []
        if not second_trip:
            return list_of_trips
        elif second_trip != '':
            for trip in list_of_trips:
                if second_trip.lower() in trip.get_second_trip().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    
    def search_depart_time_home(self, trip_object, list_of_trips):
        depart_time_home = trip_object.get_depart_time_home()
        output = []
        if not depart_time_home:
            return list_of_trips
        elif depart_time_home != '':
            for trip in list_of_trips:
                if depart_time_home.lower() in trip.get_depart_time_home().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips
    
    def search_arrival_time_dest(self, trip_object, list_of_trips):
        arrival_time_dest = trip_object.get_arrival_time_dest()
        output = []
        if not arrival_time_dest:
            return list_of_trips
        elif arrival_time_dest != '':
            for trip in list_of_trips:
                if arrival_time_dest.lower() in trip.get_arrival_time_dest().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips
    
    def search_depart_time_dest(self, trip_object, list_of_trips):
        depart_time_dest = trip_object.get_depart_time_dest()
        output = []
        if not depart_time_dest:
            return list_of_trips
        elif depart_time_dest != '':
            for trip in list_of_trips:
                if depart_time_dest.lower() in trip.get_depart_time_dest().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips
    
    def search_arrival_time_home(self, trip_object, list_of_trips):
        arrival_time_home = trip_object.get_arrival_time_home()
        output = []
        if not arrival_time_home:
            return list_of_trips
        elif arrival_time_home != '':
            for trip in list_of_trips:
                if arrival_time_home.lower() in trip.get_arrival_time_home().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips
    
    def search_status(self, trip_object, list_of_trips):
        status = trip_object.get_status()
        output = []
        if not status:
            return list_of_trips
        elif status != '':
            for trip in list_of_trips:
                if status.lower() in trip.get_status().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    def get_trips_file_headers(self):
        return DL_API().get_trips_headers()

    def find_index_in_database(self, trip_object):        
        list_of_trips = DL_API().get_trips()
        for index, trip in enumerate(list_of_trips):
            if trip.__str__() == trip_object.__str__():
                return index
        return None
    
    def edit_trip_object(self, trip_object, index):
        return DL_API().modify_trips(trip_object, index)
        
    def add_trip(self, trip_object):
        return DL_API().append_trips(trip_object)

    def ll_set_destination(self, trip_object, input_data):
        list_of_destinations = DL_API().get_destinations()
        valid = False
        for destination in list_of_destinations:
            if destination.get_destinations() == input_data:
                trip_object.set_destination(input_data)
                valid = True
        if not valid:
            return 'Destination not found. Please try again.'

    def ll_set_plane(self, trip_object, input_data):
        list_of_planes = DL_API().get_planes()
        valid = False
        for plane in list_of_planes:
            if plane.get_insignia() == input_data:                
                trip_object.set_plane(input_data)
                capacity = plane.get_capacity()
                trip_object.set_capacity(capacity)
                if not trip_object.get_captain() == '' or not trip_object.get_copilot() == '':
                    trip_object.set_captain('')
                    trip_object.set_copilot('')
                    valid = True
                    return 'Plane changed, pilots reset.'
        if valid:
            if trip_object.get_destination() != '' and trip_object.get_out_dep() != '':
                LL_Trips().create_flight_no(trip_object)
        if not valid:
            return 'Plane not found. Please try again.'
    
    def create_flight_no(self, trip_object):
        name = 'NA'
        dest = ''
        no = ''
        list_of_trips = DL_API().get_trips()
        list_of_departures = []
        list_of_destinations = DL_API().get_destinations()
        for index, destination in enumerate(list_of_destinations):
            if destination.get_airportId() == trip_object.get_destination():
              dest =   '{:02d}'.format(index)
        for trip in list_of_trips:
            if trip.get_destination() == trip_object.get_destination():
                list_of_destinations.append(trip.get_out_dep())
        list_of_departures.sort()
        for index, departure in enumerate(list_of_departures):
            if departure == trip_object.get_out_dep():
                no = str(index)
        out_flight_nr = name + dest + no
        in_flight_nr = name + dest + str(int(no)+1)
        trip_object.set_out_flight_nr(out_flight_nr)
        trip_object.set_in_flight_nr(in_flight_nr)

    def ll_set_out_dep(self, trip_object, input_data):
        if dateutil.parser.parse(input_data) == dateutil.parser.parse(input_data, yearFirst=True) == dateutil.parser.parse(input_data, dayFirst=True):
            dateutil.parser.parse(input_data)
        else:
            return "Could not understand date, plese use the format 'yyyy-mm-dd hh:mmm:ss'."
        departure = dateutil.parser.parse(input_data)
        list_of_destinations = DL_API().get_destinations()
        flight_time = ''        
        for destination in list_of_destinations:
            if destination.get_airportId() == trip_object.get_destination():
                flight_time = destination.get_flightTime()
        flight = dateutil.parser.parse(flight_time)
        iso_flight = datetime.datetime(flight.year,flight.month,flight.day,flight.hour,flight.minute,0).isoformat()
        stop = '01:00:00'
        iso_stop = datetime.datetime(stop.year, stop.month, stop.day, stop.hour, stop.minute, 0).isoformat()
        iso_out_dep = datetime.datetime(departure.year,departure.month,departure.day,departure.hour,departure.minute,0).isoformat()
        iso_in_dep = iso_out_dep + iso_flight + iso_stop
        departure_buffer = datetime.timedelta(minutes=15)
        list_of_trips = DL_API().get_trips()
        list_of_departures = []
        for trip in list_of_trips:
            temp = trip.get_out_dep()
            list_of_departures.append(dateutil.parser.parse(temp))
        for date_time in list_of_departures:
            if date_time - departure_buffer <= departure <= date_time + departure_buffer:
                return 'Another flight is scheduled for this timeslot. Please select another.'
            else:
                trip_object.set_out_dep(iso_out_dep)
                trip_object.set_in_flight_dep(iso_in_dep)
    
    def get_list_of_trips_by_employee(self, input_data):
        list_of_trips = DL_API().get_trips()
        list_of_this_employee = []
        for trip in list_of_trips:
            if trip.get_captain() == input_data:
                list_of_this_employee.append(trip)
            elif trip.get_copilot() == input_data:
                list_of_this_employee.append(trip)
            elif trip.get_fsm() == input_data:
                list_of_this_employee.append(trip)
            elif trip.get_fa1() == input_data:
                list_of_this_employee.append(trip)
            elif trip.get_fa2() == input_data:
                list_of_this_employee.append(trip)
            elif trip.get_fa3() == input_data:
                list_of_this_employee.append(trip)
            elif trip.get_fa4() == input_data:
                list_of_this_employee.append(trip)
            elif trip.get_fa5() == input_data:
                list_of_this_employee.append(trip)
        return list_of_this_employee
    
    def check_dates(self, input_data, trip_object):
        dep_out = dateutil.parser.parse(trip_object.get_out_dep())
        out_day = datetime.datetime(dep_out.year, dep_out.month, dep_out.day)
        list_of_destinations = DL_API().get_destinations()
        flight_time = ''        
        for destination in list_of_destinations:
            if destination.get_airportId() == trip_object.get_destination():
                flight_time = destination.get_flightTime()
        flight = dateutil.parser.parse(flight_time)
        dep_in = dateutil.parser.parse(trip_object.get_in_dep()) + datetime.timedelta(flight)
        in_day = datetime.datetime(dep_in.year, dep_in.month, dep_in.day)        
        list_of_trips = self.get_list_of_trips_by_employee(input_data)
        for trip in list_of_trips:
            test_dep_out = trip.get_out_dep()
            test_out_day = datetime.datetime(test_dep_out.year, test_dep_out.month, test_dep_out.day)
            flight_time = ''        
            for destination in list_of_destinations:
                if destination.get_airportId() == trip_object.get_destination():
                    flight_time = destination.get_flightTime()
            flight = dateutil.parser.parse(flight_time)
            test_dep_in = trip.get_in_dep() + datetime.timedelta(flight)
            test_in_day = datetime.datetime(dep_in.year, dep_in.month, dep_in.day)
            if test_out_day < input_data < test_in_day:
                return 'This employee is already registerd for a trip on this day.'
            else:
                return True
        
    def ll_set_captain(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()        
        list_of_captains = []
        list_of_planes = DL_API().get_planes()
        licence = ''
        list_of_licenced = []
        for plane in list_of_planes:
            if plane.get_insignia() == trip_object.get_plane():
                licence = plane.get_typeID()
        for employee in list_of_employees:
            if employee.get_rank() == 'Captain':
                list_of_captains.append(employee)
        for captain in list_of_captains:
            if captain.get_licence() == licence:
                list_of_licenced.append(captain)
        for licenced_cap in list_of_licenced:
            if licenced_cap.get_ssn() == input_data:
                if 
                trip_object.set_captain(input_data)
            else:
                return 'This is not a licenced captain. Please try again.'

    def ll_set_copilot(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()        
        list_of_copilots = []
        list_of_planes = DL_API().get_planes()
        licence = ''
        list_of_licenced = []
        for plane in list_of_planes:
            if plane.get_insignia() == trip_object.get_plane():
                licence = plane.get_typeID()
        for employee in list_of_employees:
            if employee.get_rank() == 'Copilot':
                list_of_copilots.append(employee)
        for copilot in list_of_copilots:
            if copilot.get_licence() == licence:
                list_of_licenced.append(copilot)
        for licenced_cop in list_of_licenced:
            if licenced_cop.get_ssn() == input_data:
                trip_object.set_copilot(input_data)
            else:
                return 'This is not a licenced copilot. Please try again.'

    def ll_set_fsm(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()        
        list_of_fsm = []
        for employee in list_of_employees:
            if employee.get_rank() == 'Flight Service Manager':
                list_of_fsm.append(employee)
        for fsm in list_of_fsm:
            if licenced_cop.get_ssn() == input_data:
                trip_object.set_copilot(input_data)
            else:
                return 'This is not a licenced copilot. Please try again.'
        
        
        self.set_captain(input_data)
        self.set_copilot(input_data)
        self.set_fsm(input_data)
        self.set_fa1(input_data)
        self.set_fa2(input_data)
        self.set_fa3(input_data)
        self.set_fa4(input_data)
        self.set_fa5(input_data)
        self.set_status(input_data)