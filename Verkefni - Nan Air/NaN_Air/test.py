from DataLayer.dl_api import DL_API
from LogicLayer.ll_api import LL_API
from ModelClasses.employee import Employee

# test
my_dict = {"ssn": "æaskfja"}
employee1 = Employee(my_dict)
employee2 = Employee()
employee3 = Employee("test")

search_dict = {'ssn':'', 'name':'', 'role':'', 'rank':'', 'licence':'','address':'', 'phonenumber':'', 'status':'', 'history':''}
search_criteria = Employee(search_dict)
#set1 = LL_API().search_employee(employee1)
#for i in set1:
#    print(set1)
set2 = LL_API().search_employee(search_criteria)
print(len(set2))
if len(set2) > 20:
    set4 = set2[0:20]
    print(len(set4))
for i in set4:
    print(i)




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