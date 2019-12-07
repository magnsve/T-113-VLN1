from DataLayer.dl_api import DL_API
from ModelClasses.trip import Trip


class LL_Trips():
    a flugvél og svo starfsmenn, destination,Flugnúmer beggja flugferða.
– Sætaupplýsingar, s.s. fjöldi sæta sem eru laus og fjöldi sæta sem voru seld

    def searchDestination(self, trip_object):
        # okkur vantar fleiri upplýsingar hér
        list_of_trips = DL_API().get_trips
        plane_search = self.search_plane(trip_object, list_of_trips)        
        pilot_search = self.search_pilot(trip_object, plane_search)
        cabincrew_search = self.search_cabincrew(trip_object, pilot_search)
        sold_seats_search = self.search_sold_seats(trip_object, cabincrew_search)
        available_seats_search = self.search_available_seats(trip_object, sold_seats_search)
        status_search = self.search_status(trip_object, available_seats_search)
        history_search = self.search_history(trip_object, status_search)
        return history_search


    def search_plane(self, trip_object, list_of_trips):
        plane = trip_object.get_plane()
        output = []
        if not plane:
            return list_of_trips
        elif plane != '':
            for planes in list_of_trips:
                if planes in trips.get_plane():
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
                if pilots in trips.get_pilot():
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
                if cabin in trips.get_cabincrew():
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
                if seats_sold in trips.get_sold_seats():
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
                if seats_available in trips.get_available_seats():
                    output.append(seats_available)
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

    def changeTrip():
        pass

    def searchTrip():
        pass

    def removeTrip():
        pass