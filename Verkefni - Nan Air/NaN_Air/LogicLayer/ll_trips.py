import datetime, time
import dateutil.parser
from DataLayer.dl_api import DL_API
from ModelClasses.trip import Trip

class LL_Trips():
    ''' This class handles all logic operations for the Trip object. It has several methods, some are major and are passed to the LL_API module, 
        others are minor and only used within this module. The major methods are:
        
        1)  search_trips: This method takes in a trip object and matches it to the database, one attribute at a time and then returns a list of 
            all trip objects that are a match.

        2)  get_trips_file_headers: This method reads the header row from the database by calling a method from the DL_API. Returns a list with 
            the column names.

        3)  find_index_in_database: This method takes in a trip object and loops through the database until it has a match. It then returns the 
            row index.

        4)  edit_trip_object: This method uses a trip object to replace an object from the database. It takes in a trip object and it's row index.

        5)  add_trip: This method appends a trip object to the database.

        6)  ll_set_destination: This method calls the 'set' method from the Trip model class and replaces the destination with the provided input. 
            Before it does so it searches through the destination database and checks if it is a valid destination.

        7)  ll_set_plane: This method calls the 'set' method from the Trip model class and replaces the plane with the provided input. Before it
            does so it searches through the plane database and checks if it is a valid plane. It then resets the Captain and Copilot attributes.
            If either of those were not equal to '' it returns a message stating that the Captain and Copilot have been reset.
        
        8)  create_flight_nr: This method creates the flight numbers for both the outbound and inbound flights. It uses the formula: 'NA' + 
            destination number + incremental number. This is accomplished by matching the trip's destination to the destinaton database to get
            the destination number, then creating a list of all departure times and sorting them, then using an the row number * 2 for the 
            incremental number.
            
        9)  ll_set_out_dep: This method sets the outbound flight departure time and calculates the inbound flight departure time. To do that it 
            starts by finding the flight time kept in the destination database. It does so by matching the trips destination to the database. 
            Next it compares the proposed departure time with all trips using a buffer of +- 15 min. That means that planes are able to take of 
            every 30 min. If there is anything in this process that fails to validate it returns an appropriate message.
        
        10) ll_set_captain: This method sets the captain for the flight. It begins by checking if he has a licencce for the trips plane. If so 
            it checks if he is scheduled for another trip at the same day (both departing and arriving back at Iceland).


    

        '''

    def search_trips(self, trip_object):        
        list_of_trips = DL_API().get_trips()
        destination_search = self.search_destination(trip_object, list_of_trips)
        plane_search = self.search_plane(trip_object, destination_search)        
        captain_search = self.search_captain(trip_object, plane_search)
        copilot_search = self.search_copilot(trip_object, captain_search)
        outDep_search = self.search_out_dep(trip_object, copilot_search)
        inDep_search = self.search_in_dep(trip_object, outDep_search)
        capacity_search = self.search_capacity(trip_object, inDep_search)
        inFlightNo_search = self.search_in_flight_nr(trip_object, capacity_search)
        outFlightNo_search = self.search_out_flight_nr(trip_object, inFlightNo_search)
        fsm_search = self.search_fsm(trip_object, outFlightNo_search)
        fa1_search = self.search_fa1(trip_object, fsm_search)
        fa2_search = self.search_fa2(trip_object, fa1_search)
        fa3_search = self.search_fa3(trip_object, fa2_search)
        fa4_search = self.search_fa4(trip_object, fa3_search)
        fa5_search = self.search_fa5(trip_object, fa4_search)
        status_search = self.search_status(trip_object, fa5_search)
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

    def search_copilot(self, trip_object, list_of_trips):
        copilot = trip_object.get_copilot()
        output = []
        if not copilot:
            return list_of_trips
        elif copilot != '':
            for trip in list_of_trips:
                if copilot.lower() in trip.get_copilot().lower():
                    output.append(copilot)
            return output
        else:
            return list_of_trips

    def search_capacity(self, trip_object, list_of_trips):
        capacity = trip_object.get_capacity()
        output = []
        if not capacity:
            return list_of_trips
        elif capacity != '':
            for trip in list_of_trips:
                if capacity.lower() in trip.get_capacity().lower():
                    output.append(capacity)
            return output
        else:
            return list_of_trips

    def search_in_dep(self, trip_object, list_of_trips):
        in_dep = trip_object.get_in_dep()
        output = []
        if not in_dep:
            return list_of_trips
        elif in_dep != '':
            for trip in list_of_trips:
                if in_dep.lower() in trip.get_in_dep().lower():
                    output.append(in_dep)
            return output
        else:
            return list_of_trips

    def search_out_dep(self, trip_object, list_of_trips):
        out_dep = trip_object.get_out_dep()
        output = []
        if not out_dep:
            return list_of_trips
        elif out_dep != '':
            for trip in list_of_trips:
                if out_dep.lower() in trip.get_out_dep().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    def search_in_flight_nr(self, trip_object, list_of_trips):
        in_flight_nr = trip_object.get_in_flight_nr()
        output = []
        if not in_flight_nr:
            return list_of_trips
        elif in_flight_nr != '':
            for trip in list_of_trips:
                if in_flight_nr.lower() in trip.get_in_flight_nr().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    
    def search_out_flight_nr(self, trip_object, list_of_trips):
        out_flight_nr = trip_object.get_out_flight_nr()
        output = []
        if not out_flight_nr:
            return list_of_trips
        elif out_flight_nr != '':
            for trip in list_of_trips:
                if out_flight_nr.lower() in trip.get_out_flight_nr().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips
    
    def search_fsm(self, trip_object, list_of_trips):
        fsm = trip_object.get_fsm()
        output = []
        if not fsm:
            return list_of_trips
        elif fsm != '':
            for trip in list_of_trips:
                if fsm.lower() in trip.get_fsm().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips
    
    def search_fa1(self, trip_object, list_of_trips):
        fa1 = trip_object.get_fa1()
        output = []
        if not fa1:
            return list_of_trips
        elif fa1 != '':
            for trip in list_of_trips:
                if fa1.lower() in trip.get_fa1().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips
    
    def search_fa2(self, trip_object, list_of_trips):
        fa2 = trip_object.get_fa2()
        output = []
        if not fa2:
            return list_of_trips
        elif fa2 != '':
            for trip in list_of_trips:
                if fa2.lower() in trip.get_fa2().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    def search_fa3(self, trip_object, list_of_trips):
        fa3 = trip_object.get_fa3()
        output = []
        if not fa3:
            return list_of_trips
        elif fa3 != '':
            for trip in list_of_trips:
                if fa3.lower() in trip.get_fa3().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    def search_fa4(self, trip_object, list_of_trips):
        fa4 = trip_object.get_fa4()
        output = []
        if not fa4:
            return list_of_trips
        elif fa4 != '':
            for trip in list_of_trips:
                if fa4.lower() in trip.get_fa4().lower():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    def search_fa5(self, trip_object, list_of_trips):
        fa5 = trip_object.get_fa5()
        output = []
        if not fa5:
            return list_of_trips
        elif fa5 != '':
            for trip in list_of_trips:
                if fa5.lower() in trip.get_fa5().lower():
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
            if trip.__str__().lower() == trip_object.__str__().lower():
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
            if destination.get_airport_id().lower() == input_data.lower():
                trip_object.set_destination(input_data)
                valid = True
        if not valid:
            return 'Destination not found. Please try again.'

    def ll_set_plane(self, trip_object, input_data):
        if trip_object.get_out_dep() != '':
            list_of_planes = DL_API().get_planes()
            valid = False
            for plane in list_of_planes:
                if plane.get_insignia().lower() == input_data.lower():
                    trip_object.set_plane(input_data.upper())
                    capacity = plane.get_capacity()
                    trip_object.set_capacity(capacity)
                    self.setStatus(trip_object)
                    if not trip_object.get_captain() == '' or not trip_object.get_copilot() == '':
                        trip_object.set_captain('')
                        trip_object.set_copilot('')
                    valid = True                        
            if valid:
                if trip_object.get_destination() != '' and trip_object.get_out_dep() != '':
                    self.create_flight_nr(trip_object)
            else:
                return 'Plane not found. Please try again.'
        else:
            return 'You need to set the date before you can set the plane.'
    
    def create_flight_nr(self, trip_object):
        name, dest, no = 'NA', 0, 0
        list_of_destinations, list_of_trips, list_of_departures = DL_API().get_destinations(), DL_API().get_trips(), []
        for index, destination in enumerate(list_of_destinations):
            if destination.get_airport_id().lower() == trip_object.get_destination().lower():
                dest = '{:02d}'.format(index+1)
        for trip in list_of_trips:
            if trip.get_destination() == trip_object.get_destination():
                list_of_departures.append(trip.get_out_dep())
        list_of_departures.sort()
        for index, departure in enumerate(list_of_departures):
            if departure == trip_object.get_out_dep():
                no = index * 2
        out_flight_nr = name + dest + str(no)
        in_flight_nr = name + dest + str(no + 1)
        trip_object.set_out_flight_nr(out_flight_nr)
        trip_object.set_in_flight_nr(in_flight_nr)

    def ll_set_out_dep(self, trip_object, input_data):
        try:
            dateutil.parser.parse(input_data)            
        except ValueError:
            return "Could not understand date, plese use the format 'yyyy-mm-dd hh:mmm:ss'."        
        if trip_object.get_destination() != '':
            departure = dateutil.parser.parse(input_data)
            list_of_destinations = DL_API().get_destinations()
            flight_time = ''        
            for destination in list_of_destinations:
                if destination.get_airport_id().lower() == trip_object.get_destination().lower():
                    flight_time = destination.get_flight_time()            
            flight_hours, flight_minutes, flight_seconds = flight_time.split(':')
            flight = datetime.timedelta(hours=int(flight_hours), minutes=int(flight_minutes), seconds=int(flight_seconds))            
            stop = datetime.timedelta(hours=1)                        
            iso_out_dep = datetime.datetime(departure.year,departure.month,departure.day,departure.hour,departure.minute,0).isoformat()
            in_dep = departure + flight + stop
            iso_in_dep = datetime.datetime(in_dep.year,in_dep.month,in_dep.day,in_dep.hour,in_dep.minute,0).isoformat()
            departure_buffer = datetime.timedelta(minutes=15)
            list_of_trips = DL_API().get_trips()
            list_of_departures = []
            for trip in list_of_trips:
                temp = trip.get_out_dep()
                if temp != '':
                    list_of_departures.append(dateutil.parser.parse(temp))
            if len(list_of_departures):
                for date_time in list_of_departures:
                    if date_time - departure_buffer <= departure <= date_time + departure_buffer:
                        return 'Another flight is scheduled for this timeslot. Please select another.'
                    else:
                        trip_object.set_out_dep(iso_out_dep)
                        trip_object.set_in_dep(iso_in_dep)
            else:
                trip_object.set_out_dep(iso_out_dep)
                trip_object.set_in_dep(iso_in_dep)
            self.setStatus(trip_object)
        else: 
            return 'You have to set a destination before you select the departure time.'
    
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
        flight_times = []
        for destination in list_of_destinations:
            if destination.get_airport_id() == trip_object.get_destination():
                flight_times.append(destination.get_flight_time().split(':'))
        for flight in flight_times:
            flight_hours, flight_minutes, flight_seconds = flight
            flight = datetime.timedelta(hours=int(flight_hours), minutes=int(flight_minutes), seconds=int(flight_seconds))
            dep_in = dateutil.parser.parse(trip_object.get_in_dep()) + datetime.timedelta(flight)
            in_day = datetime.datetime(dep_in.year, dep_in.month, dep_in.day)
            list_of_trips = self.get_list_of_trips_by_employee(input_data)
            for trip in list_of_trips:
                test_dep_out = trip.get_out_dep()
                test_out_day = datetime.datetime(test_dep_out.year, test_dep_out.month, test_dep_out.day)
                flight_time = ''
                for destination in list_of_destinations:
                    if destination.get_airport_id() == trip_object.get_destination():
                        flight_time = destination.get_flight_time()
                        flight_hours, flight_minutes, flight_seconds = flight_time.split(':')
                        flight = datetime.timedelta(hours=int(flight_hours), minutes=int(flight_minutes), seconds=int(flight_seconds))                        
                    test_dep_in = trip.get_in_dep() + datetime.timedelta(flight)
                    test_in_day = datetime.datetime(test_dep_in.year, test_dep_in.month, test_dep_in.day)
                    if out_day <= test_out_day <= in_day or out_day <= test_in_day <= in_day:
                        return 'This employee is already registerd for a trip on this day.'
        else:
            return True
        
    def ll_set_captain(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()
        list_of_captains = []
        list_of_planes = DL_API().get_planes()
        licence = ''
        valid = False
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
                if self.check_dates(input_data, trip_object):
                    trip_object.set_captain(input_data)
                    self.setStatus(trip_object)                    
                    valid = True
                else:
                    return 'This captain is working on this day.'
        if not valid:
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
                if self.check_dates(input_data, trip_object):
                    trip_object.set_copilot(input_data)
                    self.setStatus(trip_object)
            else:
                return 'This is not a licenced copilot. Please try again.'

    def ll_set_fsm(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()        
        list_of_fsm = []
        for employee in list_of_employees:
            if employee.get_rank() == 'Flight Service Manager':
                list_of_fsm.append(employee)
        for fsm in list_of_fsm:
            if fsm.get_ssn() == input_data:
                if self.check_dates(input_data, trip_object):
                    trip_object.set_fsm(input_data)
                    self.setStatus(trip_object)
            else:
                return 'This is not a Flight Service Manager. Please try again.'
    
    def ll_set_fa1(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()        
        list_of_fa = []
        for employee in list_of_employees:
            if employee.get_rank() == 'Flight Attendant':
                list_of_fa.append(employee)
        for fa in list_of_fa:
            if fa.get_ssn() == input_data:
                if self.check_dates(input_data, trip_object):
                    trip_object.set_fa1(input_data)
                    self.setStatus(trip_object)
            else:
                return 'This is not a Flight Attendant. Please try again.'
    
    def ll_set_fa2(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()        
        list_of_fa = []
        for employee in list_of_employees:
            if employee.get_rank() == 'Flight Attendant':
                list_of_fa.append(employee)
        for fa in list_of_fa:
            if fa.get_ssn() == input_data:
                if self.check_dates(input_data, trip_object):
                    trip_object.set_fa2(input_data)
                    self.setStatus(trip_object)
            else:
                return 'This is not a Flight Attendant. Please try again.'
        
    def ll_set_fa3(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()        
        list_of_fa = []
        for employee in list_of_employees:
            if employee.get_rank() == 'Flight Attendant':
                list_of_fa.append(employee)
        for fa in list_of_fa:
            if fa.get_ssn() == input_data:
                if self.check_dates(input_data, trip_object):
                    trip_object.set_fa3(input_data)
                    self.setStatus(trip_object)
            else:
                return 'This is not a Flight Attendant. Please try again.'
        
    def ll_set_fa4(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()        
        list_of_fa = []
        for employee in list_of_employees:
            if employee.get_rank() == 'Flight Attendant':
                list_of_fa.append(employee)
        for fa in list_of_fa:
            if fa.get_ssn() == input_data:
                if self.check_dates(input_data, trip_object):
                    trip_object.set_fa4(input_data)
                    self.setStatus(trip_object)
            else:
                return 'This is not a Flight Attendant. Please try again.'

    def ll_set_fa5(self, trip_object, input_data):
        list_of_employees = DL_API().get_employees()        
        list_of_fa = []
        for employee in list_of_employees:
            if employee.get_rank() == 'Flight Attendant':
                list_of_fa.append(employee)
        for fa in list_of_fa:
            if fa.get_ssn() == input_data:
                if self.check_dates(input_data, trip_object):
                    trip_object.set_fa5(input_data)
                    self.setStatus(trip_object)
            else:
                return 'This is not a Flight Attendant. Please try again.'
    
    def setStatus(self, trip):
        if trip.get_out_dep() == '':
            pass
        else:            
            out_departure = dateutil.parser.parse(trip.get_out_dep())        
            in_departure = dateutil.parser.parse(trip.get_in_dep())
            stop = datetime.timedelta(hours=1)            
            flight_time = in_departure - out_departure - stop
            out_arrival = out_departure + flight_time
            in_arrival = in_departure + flight_time
            now = datetime.datetime.now()
            status = ''
            if now < out_departure:
                status = 'Not started'
            elif out_departure <= now < out_arrival:
                status = 'In the air'
            elif out_arrival <= now < in_departure:
                status = 'At destination'
            elif in_departure <= now < in_arrival:
                status = 'In the air'
            else:
                status = 'Flight completed'
            return trip.set_status(status)

    def ll_set_out_flight_nr(self, trip_object, input_data):
        pass

    def ll_set_in_flight_nr(self, trip_object, input_data):
        pass
    
    def ll_set_in_dep(self, trip_object, input_data):
        pass

    def ll_set_capacity(self, trip_object, input_data):
        pass

    def ll_set_status(self, trip_object, input_data):
        pass