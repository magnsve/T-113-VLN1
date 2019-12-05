import csv
from LogicLayer import LL_API

dataBase = "prufaverklegt.csv"
ssn = "170194-3069"
def read_file(filepath = dataBase):
    emptylist = []
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            emptylist.append(row)
        return(emptylist)

readingfile = read_file(filepath = dataBase)

def find_index(ssn,filepath = dataBase): 
    with open(filepath) as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1:] for rows in reader}
        if ssn in mydict:
            return 

Data = Employee()

def testing(Data, filepath = dataBase):
    input_file = csv.DictReader(open(dataBase))
    for row in input_file:
        if row['ssn'] == Data.get_ssn():
            try:
                csv.DictWriter
                return True
            except errro:
                return False

def read_Employees():
    input_file = csv.DictReader(open(dataBase))
    output = []
    for row in input_file:
        data = Employee(row)
        output.append(data)
    return output



findindex = find_index(ssn)

#print(readingfile)
#print(findindex)
print(testing(ssn))