from DataLayer.dl_api import DL_API
from LogicLayer.ll_api import LL_API
from ModelClasses.employee import Employee

# test
my_dict = {"ssn": "æaskfja"}
employee1 = Employee(my_dict)
employee2 = Employee()
employee3 = Employee("test")

print(employee1)
print(employee2)
print(employee3)
print(employee1.get_ssn())
print(employee2.get_ssn())
print(employee3.get_ssn())
LL_API().inactivate_employee(employee3,1)
employees = DL_API().get_employees()
for elem in employees:
    print(elem)



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