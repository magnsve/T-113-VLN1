from  import Planes

planesDict = {'plane_insignia': 'TF-LIF',\
    'plane_type_id': 'F100',\
    'plane_manufacturer': 'Magnús',\
    'plane_model':'Good',\
    'plane_capacity':'mucho'}

flugvel = Planes(planesDict)
print(flugvel.get_insignia())