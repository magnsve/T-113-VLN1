c = '+'
v = '|'
h = '-'

filestream = open('Header.txt','r')
header = []
for line in filestream:
    header.append(line.strip('\n'))

print(c + h*78 + c)
for line in header:
    print(c + line.center(78,h) + c)
print(c + h * 78 + c)
print(v + "Welcome to your NaN Air Manager".center(78) + v)
print(v+" ".center(78)+v)
print(v + "To continue, please select an option from the menu.".center(78) + v)
print( c + h * 78 + c)
print( v + "1 - Employee management".center(78) + v)
print( v + "2 - Airplane management".center(78) + v)
print( v + "3 - Destination management".center(78) + v)
print( v + "3 - Trip management".center(78) + v)
for i in range(1, 3):
    print( v + " " * 78 + v)
print( c + h * 78 + c)

inputa = input(" "*32 + "Your choice: ")

sys.stdin.read(1)