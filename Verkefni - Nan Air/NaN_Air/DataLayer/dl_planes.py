#imports and constants
import csv
from ModelClasses.plane import Plane

#Classes
class DL_Planes():
    ''' '''
    FILE_NAME = 'DataLayer\\DL_Database\\Aircraft.csv'

    def getPlanes(self):
        _file = csv.DictReader(open(self.FILE_NAME))
        output = []
        for row in _file:
            data = Plane(row)
            output.append(data)
        return output

    def appendPlanes(self, plane_object):
        with open(self.FILE_NAME, 'a') as _file:
            _file.write(plane_object.__str__())
        return True 

    def modifyPlanes(self, plane_object, index):
        lines = open(self.FILE_NAME).read().splitlines()
        print(lines)
        print(plane_object.__str__())
        lines[index] = plane_object.__str__()
        open(self.FILE_NAME,'w').write('\n'.join(lines))
        return True

    def get_headers_plane(self):
        with open(self.FILE_NAME) as _file:
            dict_reader = csv.DictReader(_file)
            return dict_reader.fieldnames