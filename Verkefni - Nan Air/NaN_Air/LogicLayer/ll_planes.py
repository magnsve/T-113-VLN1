from DataLayer.dl_api import DL_API
from ModelClasses.plane import Plane

class LL_Planes():

    #nafn, tegund, framleiðandi og fjöldi farþegasæta.
    def search_plane(self, plane_object):
        list_of_planes = DL_API().get_planes()
        insignia_search = self.search_insignia(plane_object, list_of_planes)        
        typeID_search = self.search_typeID(plane_object, insignia_search)
        manufacturer_search = self.search_manufacturer(plane_object, typeID_search)
        model_search = self.search_model(plane_object, manufacturer_search)
        capacity_search = self.search_capacity(plane_object, model_search)
        return capacity_search

    def search_insignia(self, plane_object, list_of_planes):
        insignia = plane_object.get_insignia()
        output = []
        if not insignia:
            return list_of_planes
        elif insignia != '':
            for plane in list_of_planes:
                if insignia.lower() in plane.get_insignia().lower():
                    output.append(plane)
            return output
        else:
            return list_of_planes


    def search_typeID(self, plane_object, list_of_planes):
        typeID = plane_object.get_typeID()
        output = []
        if not typeID:
            return list_of_planes
        elif typeID != '':
            for plane in list_of_planes:
                if typeID.lower() in plane.get_typeID().lower():
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
                if capacity.lower() in plane.capacity().lower():
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
                if manufacturer.lower() in plane.get_manufacturer().lower():
                    output.append(plane)
            return output
        else:
            return list_of_planes

    def search_model(self, plane_object, list_of_planes):
        model = plane_object.get_model()
        output = []
        if not model:
            return list_of_planes
        elif model != '':
            for plane in list_of_planes:
                if model.lower() in plane.get_model().lower():
                    output.append(plane)
            return output
        else:
            return list_of_planes

    def get_plane_file_headers(self):
        return DL_API().get_plane_headers()

    def find_index_in_database(self, plane_object):
        list_of_planes = DL_API().get_planes()
        for index, plane in enumerate(list_of_planes):
            if plane.__str__() == plane_object.__str__():
                return index
        return None
    
    def edit_plane_object(self, plane_object, index):
        return DL_API().modify_planes(plane_object, index)
        
    def add_plane(self, plane_object):
        return DL_API().append_planes(plane_object)

    def ll_set_insignia(self, plane_object, input_data):
        return plane_object.set_insignia(input_data)

    def ll_set_typeID(self, plane_object, input_data):
        return plane_object.set_typeID(input_data)
        
    def ll_set_manufacturer(self, plane_object, input_data):
        return plane_object.set_manufacturer(input_data)

    def ll_set_model(self, plane_object, input_data):
        return plane_object.set_model(input_data)

    def ll_set_capacity(self, plane_object, input_data):
        return plane_object.set_capacity(input_data)