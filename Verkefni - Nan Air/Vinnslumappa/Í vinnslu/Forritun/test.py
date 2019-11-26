c = '+'
v = '|'
h = '-'
s = ' '

input_raw(test)

filestream = open('Header.txt','r')
header = []
for line in filestream:
    header.append(line.strip('\n'))

for i in range(20):
    print()
print(c + h*78 + c)
for line in header:
    print(c + line.center(78,h) + c)
print(c + h * 78 + c)
print(v + "Welcome to your NaN Air Managers home page.".center(78) + v)
print(v+" ".center(78)+v)
print(v + "To continue, please select an option from the menu.".center(78) + v)
print( c + h * 78 + c)
print( v + s * 5 + "1 - Employee management".ljust(73) + v)
print( v + s * 5 + "2 - Airplane management".ljust(73) + v)
print( v + s * 5 + "3 - Destination management".ljust(73) + v)
print( v + s * 5 + "4 - Trip management".ljust(73) + v)
for i in range(1, 3):
    print( v + s * 78 + v)
print(v + "Type 'Quit' to exit.".rjust(73) + s * 5 + v)
print( c + h * 78 + c)


inputa = input(" "*32 + "Your choice: ")
