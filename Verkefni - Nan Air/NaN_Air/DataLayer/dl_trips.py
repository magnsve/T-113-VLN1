# Imports and constants
import csv, codecs
from ModelClasses.trip import Trip

# Classes
class DL_Trips():
    ''' This class handles the database for Trips. It has four methods:
        
        1) getTrips:        This method reads the database and returns each line as a Trip object.
        2) appendTrips:     This method appends a Trip object to the bottom of the database.
        3) modifyTrip:      This method writes over an entry in the database. 
        4) getTripsHeaders: This method returns a list with the header row. '''
        
    FILE_NAME = 'DataLayer\\DL_Database\\Employees.csv'
    ENCODING = 'utf-8'

    def getTrips(self):
        output = []
        with codecs.open(self.FILE_NAME, 'r', self.ENCODING) as _file:
            reader = csv.reader(_file)
            headers = next(reader)
            for row in reader:
                row_dict = dict(zip(headers,row))
                trip_from_row = Trip(row_dict)
                output.append(trip_from_row)
        return output

    def appendTrips(self, trip_object):
        with codecs.open(self.FILE_NAME, 'a', self.ENCODING) as _file:
            _file.write(trip_object.__str__())        

    def modifyTrip(self, trip_object, index):
        list_of_trips = self.getTrips()
        headers = self.getTripsHeaders()
        with codecs.open(self.FILE_NAME, 'w', self.ENCODING) as _file:
            writer = csv.writer(_file)
            list_of_trips[index] = trip_object
            output = [headers]
            for trip in list_of_trips:
                value_list = trip.__str__().split(',')
                output.append(value_list)
            for row in output:
                writer.writerow(row)

    def getTripsHeaders(self):
        with open(self.FILE_NAME, encoding="utf-8-sig") as _file:
            dict_reader = csv.DictReader(_file)            
            return dict_reader.fieldnames