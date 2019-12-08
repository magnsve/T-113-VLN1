from DataLayer.dl_api import DL_API
from ModelClasses.plane import Plane

class LL_Planes():

    def changePlane(self):
        pass
    #nafn, tegund, framleiðandi og fjöldi farþegasæta.
    def searchPlane(self, plane_object):
        list_of_planes = DL_API().get_planes    
        insignia_search = self.search_insignia(plane_object, list_of_planes)        
        type_search = self.search_type(plane_object, name_search)
        manufacturer_search = self.search_manufacturer(plane_object, type_search)
        capacity_search = self.search_capacity(plane_object, manufacturer_search)
        status_search = self.search_status(plane_object, no_seats_search)
        history_search = self.search_history(plane_object, status_search)
        return history_search

    def search_insignia(self, plane_object, list_of_planes):
        insignia = plane_object.get_insignia()
        output = []
        if not insignia:
            return list_of_planes
        elif insignia != '':
            for plane in list_of_planes:
                if insignia in plane.get_insignia():
                    output.append(plane)
            return output
        else:
            return list_of_planes


    def search_type(self, plane_object, list_of_planes):
        Type = plane_object.get_type()
        output = []
        if not Type:
            return list_of_planes
        elif Type != '':
            for plane in list_of_planes:
                if Type in plane.get_type():
                    output.append(plane)
            return output
        else:
            return list_of_planes
    
    def search_capacity(self, plane_object, list_of_planes):
        capacity = plane_object.get_capacity()
        output = []
        if not capacity:
            return list_of_planes
        elif capacity != '':
            for plane in list_of_planes:
                if capacity in plane.capacity():
                    output.append(plane)
            return output
        else:
            return list_of_planes


    def search_manufacturer(self, plane_object, list_of_planes):
        manufacturer = plane_object.get_manufacturer()
        output = []
        if not manufacturer:
            return list_of_planes
        elif manufacturer != '':
            for plane in list_of_planes:
                if manufacturer in plane.get_type():
                    output.append(plane)
            return output
        else:
            return list_of_planes

    def search_history(self, plane_object, list_of_planes):
        history = plane_object.get_history()
        output = []
        if not history:
            return list_of_planes
        elif history != '':
            for plane in list_of_planes:
                if history in plane.get_history():
                    output.append(plane)
            return output
        else:
            return list_of_planes

    def search_status(self, plane_object, list_of_planes):
        status = plane_object.get_status()
        output = []
        if not status:
            return list_of_planes
        elif status != '':
            for plane in list_of_planes:
                if status in plane.get_status():
                    output.append(plane)
            return output
        else:
            return list_of_planes

    def inactivatePlane(self, plane_object, index):
        plane_object.set_status('inactive')        
        DL_API().modify_planes(plane_object, index)

    def get_headers(self):
        return DL_API().get_headers()
    
    def removePlane(self):
        pass

    def changePlane():
        pass
