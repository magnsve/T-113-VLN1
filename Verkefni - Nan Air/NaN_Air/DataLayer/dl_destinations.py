#imports and constants
import csv, codecs
from ModelClasses.destination import Destination

#Classes
class DL_Destinations():
    ''' This class handles the database for Destinations. It has four methods:
        
        1) getDestinations:         This method reads the database and returns each line as a Destination object.
        2) appendDestinations:      This method appends a Destination object to the bottom of the database.
        3) modifyDestinations:      This method writes over an entry in the database. 
        4) getDestinationsHeaders:  This method returns a list with the header row. '''

    FILE_NAME = "DataLayer\\DL_Database\\Destinations.csv"
    ENCODING = 'utf-8'

    def getDestinations(self):
        output = []
        with codecs.open(self.FILE_NAME, 'r', self.ENCODING) as _file:
            reader = csv.reader(_file)
            headers = next(reader)
            for item in headers:
                if item == 'flight time':
                    item = 'flight_time'
                elif item == 'ice number':
                    item = 'ice_number'
            for row in reader:
                row_dict = dict(zip(headers,row))
                destinations_from_row = Destination(row_dict)
                output.append(destinations_from_row)
        return output

    def appendDestinations(self, destination_object):
        with codecs.open(self.FILE_NAME, 'a', self.ENCODING) as _file:
            _file.write(destination_object.__str__())
        return True 
    
    def modifyDestinations(self, destination_object, index):
        list_of_destinations = self.getDestinations()
        headers = self.getDestinationsHeaders()
        with codecs.open(self.FILE_NAME, 'w', self.ENCODING) as _file:
            writer = csv.writer(_file)
            list_of_destinations[index] = destination_object
            output = [headers]
            for destination in list_of_destinations:
                value_list = destination.__str__().split(',')
                output.append(value_list)
            for row in output:
                writer.writerow(row)

    def getDestinationsHeaders(self):
        with open(self.FILE_NAME, encoding="utf-8-sig") as _file:
            dict_reader = csv.DictReader(_file)            
            return dict_reader.fieldnames