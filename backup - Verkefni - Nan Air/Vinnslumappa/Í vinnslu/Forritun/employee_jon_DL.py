import csv
from logicLayer.employeedata import Employee

class employee:
    dataBase = "prufaverklegt.csv"
    def read_file(self,filepath = dataBase):
        emptylist = []
        with open(filepath) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                instance = Employee(row)
                emptylist.append[instance]
            print(emptylist)

    def set_employee(self,filepath,Employee):
        data = Prepare_for_csv()
        with open(filepath,'a') as f:
            writer=csv.writer(f)
            writer.writerow(data)
            return f


    def Modify_employee(Employee,index):
        data = change_employee()
        index = find_index()
        with open(filepath,'a') as f:
            writer=csv.writer(f)
            writer.writerow(data)
            for index, row in filepath:
                
        def find_index(ssn): 
            with open(filepath,'a') as f: 
                data = csv.reader(f) 
                index = 0 
                for row in data:
                    if row[0] == ssn
                        return index 
                    else : index+=1
                return index
def main():
    emplo_yee = Employee()
    reading = emplo_yee.read_file()

main()