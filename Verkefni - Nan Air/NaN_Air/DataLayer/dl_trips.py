# Imports and constants
import csv
from ModelClasses.trip import Trip

# Classes
class DL_Trips():
    ''' '''
    FILE_NAME = ""
    #Þarf að bæta við skrá sem heldur utan um Trips. 

    def getTrips(self):
        _file = csv.DictReader(open(self.FILE_NAME))
        output = []
        for row in _file:
            data = Trip(row)
            output.append(data)
        return output

    def appendTrips(self, trip_object):
        with open(self.FILE_NAME, 'a') as _file:
            _file.write(trip_object.__str__())
        return True 

    def modifyTrips(self, trip_object, index):
        lines = open(self.FILE_NAME).read().splitlines()
        print(lines)
        print(trip_object.__str__())
        lines[index] = trip_object.__str__()
        open(self.FILE_NAME,'w').write('\n'.join(lines))
        return True

    def get_headers_trips(self):
        with open(self.FILE_NAME) as _file:
            dict_reader = csv.DictReader(_file)
            return dict_reader.fieldnames