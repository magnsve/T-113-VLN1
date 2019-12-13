# Imports and constants
import csv, codecs, dateutil.parser, datetime
from ModelClasses.trip import Trip
from .dl_destinations import DL_Destinations

# Classes
class DL_Trips():
    ''' This class handles the database for Trips. It has four methods:
        
        1) getTrips:        This method reads the database and returns each line as a Trip object.
        2) appendTrips:     This method appends a Trip object to the bottom of the database.
        3) modifyTrip:      This method writes over an entry in the database. 
        4) getTripsHeaders: This method returns a list with the header row. '''
        
    FILE_NAME = 'DataLayer\\DL_Database\\Trips.csv'
    ENCODING = 'utf-8'

    def getTrips(self):
        output = []
        with codecs.open(self.FILE_NAME, 'r', self.ENCODING) as _file:
            reader = csv.reader(_file)
            headers = next(reader)
            headers2 = []
            for item in headers:
                if item == 'out. flight nr':
                    headers2.append('out_flight_nr')
                elif item == 'out. dep':
                    headers2.append('out_dep')
                elif item == 'in. flight nr':
                    headers2.append('in_flight_nr')
                elif item == 'in. dep':
                    headers2.append('in_dep')
                else:
                    headers2.append(item)
            for row in reader:
                row_dict = dict(zip(headers2,row))
                trip_from_row = Trip(row_dict)
                self.setStatus(trip_from_row)
                output.append(trip_from_row)
        return output

    def appendTrips(self, trip_object):
        with codecs.open(self.FILE_NAME, 'a', self.ENCODING) as _file:
            header = self.getTripsHeaders()
            for item in header:
                if item == 'out. flight nr':
                    item = 'out_flight_nr'
                elif item == 'out. dep':
                    item = 'out_dep'
                elif item == 'in. flight nr':
                    item = 'in_flight_nr'
                elif item == 'in. dep':
                    item = 'in_dep'
            new_row = trip_object.__dict__
            output = ''
            for key, value in new_row.items():
                for item in header:
                    if key.replace('_Trip__','') == item:
                        output += '{},'.format(value)
            _file.write(output)

    def modifyTrip(self, trip_object, index):
        list_of_trips = self.getTrips()
        headers = self.getTripsHeaders()
        headers2 = []
        for item in headers:
            if item == 'out. flight nr':
                headers2.append('out_flight_nr')
            elif item == 'out. dep':
                headers2.append('out_dep')
            elif item == 'in. flight nr':
                headers2.append('in_flight_nr')
            elif item == 'in. dep':
                headers2.append('in_dep')
            else:
                headers2.append(item)
        with codecs.open(self.FILE_NAME, 'w', self.ENCODING) as _file:
            writer = csv.writer(_file)
            list_of_trips[index] = trip_object
            output = [headers]
            for trip in list_of_trips:                
                for index, item in enumerate(headers2):
                    if item == 'out. flight nr':
                        item = 'out_flight_nr'
                    elif item == 'out. dep':
                        item = 'out_dep'
                    elif item == 'in. flight nr':
                        item = 'in_flight_nr'
                    elif item == 'in. dep':
                        item = 'in_dep'
                new_row = trip.__dict__
                temp = ''
                for key, value in new_row.items():
                    for item in headers2:
                        if key.replace('_Trip__','') == item:
                            temp += '{},'.format(value)
                value_list = temp.split(',')
                output.append(value_list)            
            for row in output:
                writer.writerow(row)                     

    def getTripsHeaders(self):
        with open(self.FILE_NAME, encoding="utf-8-sig") as _file:
            dict_reader = csv.DictReader(_file)            
            return dict_reader.fieldnames
    
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