from DataLayer.dl_api import DL_API
from LogicLayer.ll_api import LL_API
from ModelClasses.employee import Employee
from ModelClasses.destination import Destination
from InterfaceLayer.il_employee_search_menu import IL_EmployeeSearchMenu

# header_row = LL_API().get_employee_header()
# for item in header_row:
#     print(item)
# header_row.sort()
# print()
# for item in header_row:
#     print(item)

x = Employee('test')
print(x.__dict__)
print(x.__dict__.keys())
print(x.__dict__.values())

# get_list = IL_EmployeeSearchMenu().list_of_get_functions(x)
# set_list = IL_EmployeeSearchMenu().list_of_set_functions(x)
# for item in get_list:    
#     print(item)
#     method_ = getattr(x, item)
#     print(method_())


# search_dict = {'airportId':'11', 'destination':'1', 'country':'2', 'flightTime':'3', 'distance':'4','emergencyContact':'5', 'emergencyContactNumber':'6', 'status':'7', 'history':'8'}
# print(DL_API().get_headers_destinations())
# new_destination = Destination(search_dict)
# print(new_destination)
# DL_API().modify_destinations(new_destination, 8)

# destinations = DL_API().get_destinations()
# for i in destinations:
#     print(i)





# test
# my_dict = {"ssn": "æaskfja"}
# employee1 = Employee(my_dict)
# employee2 = Employee()
# employee3 = Employee("test")

# search_dict = {'ssn':'', 'name':'John', 'role':'', 'rank':'', 'licence':'','address':'', 'phonenumber':'', 'status':'', 'history':''}
# test = Employee()
# test.set_name('John')
# search_criteria = Employee(search_dict)
#set1 = LL_API().search_employee(employee1)
#for i in set1:
#    print(set1)
# set2 = LL_API().search_employee(test)
# print(len(set2))
# for i in set2:
#     print(i)

# if len(set2) > 20:
#     set4 = set2[0:20]
#     print(len(set4))
# for i in set4:
#     print(i)




#print(employee1)
#print(employee2)
#print(employee3)
# print(employee1.get_ssn())
# test = LL_API().get_employee_header()
# for item in test:
#     print(item.capitalize())
# print(test)
#print(employee1.__dict__.keys())
#print(employee2.get_ssn())
#print(employee3.get_ssn())
#LL_API().inactivate_employee(employee3,1)
#employees = DL_API().get_employees()
#for elem in employees:
#    print(elem)



# employees = DL_API().get_employees()
# for element in employees:
#     print(element)

# DL_API().append_employee(employee3)
# employees = DL_API().get_employees()
# for element in employees:
#     print(element)

# DL_API.modify_employee(employee,4)
# employee = DL_API.get_employees()
# for element in employees:
#     print(element)
