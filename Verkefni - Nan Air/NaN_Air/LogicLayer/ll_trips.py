from DataLayer.dl_api import DL_API
from ModelClasses.trip import Trip
from .ll_employee import LL_Employee


class LL_Trips():
    
    def searchtrips(self, trip_object):
        # okkur vantar fleiri upplýsingar hér
        list_of_trips = DL_API().get_trips
        destination_search = self.search_destination(trip_object, list_of_trips)
        plane_search = self.search_plane(trip_object, destination_search)        
        pilot_search = self.search_pilot(trip_object, plane_search)
        cabincrew_search = self.search_cabincrew(trip_object, pilot_search)
        sold_seats_search = self.search_sold_seats(trip_object, cabincrew_search)
        available_seats_search = self.search_available_seats(trip_object, sold_seats_search)
        first_trip_search = self.search_first_trip(trip_object, available_seats_search)
        second_trip_search = self.search_second_trip(trip_object, first_trip_search)
        depart_time_home_search = self.search_depart_time_home
        arrival_time_dest_search = self.search_arrival_time_dest
        depart_time_dest_search = self.search_depart_time_dest
        arrival_time_home = self.search_arrival_time_home
        status_search = self.search_status(trip_object, second_trip_+search)
        history_search = self.search_history(trip_object, status_search)
        return history_search

    def search_destination(self, trip_object, list_of_trips):
        destination = trip_object.get_destination()
        output = []
        if not destination:
            return list_of_trips
        elif destination != '':
            for destinations in list_of_trips:
                if destinations in trip.get_destination():
                    output.append(destinations)
            return output
        else:
            return list_of_trips

    def search_plane(self, trip_object, list_of_trips):
        plane = trip_object.get_plane()
        output = []
        if not plane:
            return list_of_trips
        elif plane != '':
            for planes in list_of_trips:
                if planes in trip.get_plane():
                    output.append(planes)
            return output
        else:
            return list_of_trips

    def search_pilot(self, trip_object, list_of_trips):
        pilot = trip_object.get_pilot()
        output = []
        if not pilot:
            return list_of_trips
        elif pilot != '':
            for pilots in list_of_trips:
                if pilots in trip.get_pilot():
                    output.append(pilots)
            return output
        else:
            return list_of_trips

    def search_cabincrew(self, trip_object, list_of_trips):
        cabincrew = trip_object.get_cabincrew()
        output = []
        if not cabincrew:
            return list_of_trips
        elif cabincrew != '':
            for cabin in list_of_trips:
                if cabin in trip.get_cabincrew():
                    output.append(cabin)
            return output
        else:
            return list_of_trips

    def search_sold_seats(self, trip_object, list_of_trips):
        sold_seats = trip_object.get_sold_seats()
        output = []
        if not sold_seats:
            return list_of_trips
        elif sold_seats != '':
            for seats_sold in list_of_trips:
                if seats_sold in trip.get_sold_seats():
                    output.append(seats_sold)
            return output
        else:
            return list_of_trips

    def search_available_seats(self, trip_object, list_of_trips):
        available_seats = trip_object.get_available_seats()
        output = []
        if not available_seats:
            return list_of_trips
        elif available_seats != '':
            for seats_available in list_of_trips:
                if seats_available in trip.get_available_seats():
                    output.append(seats_available)
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
                if first_trip in trip.get_first_trip():
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
                if second_trip in trip.get_second_trip():
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
                if depart_time_home in trip.get_depart_time_home():
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
                if arrival_time_dest in trip.get_arrival_time_dest():
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
                if depart_time_dest in trip.get_depart_time_dest():
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
                if arrival_time_home in trip.get_arrival_time_home():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    def search_history(self, trip_object, list_of_trips):
        history = trip_object.get_history()
        output = []
        if not history:
            return list_of_trips
        elif history != '':
            for trip in list_of_trips:
                if history in trip.get_history():
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
                if status in trip.get_status():
                    output.append(trip)
            return output
        else:
            return list_of_trips

    def check_licence(trip_obj):
        employees = DL_API().get_employees()
        return LL_Employee().search_licence(trip_obj, employees)
