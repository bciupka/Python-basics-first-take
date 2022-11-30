string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for a in range(10):
    print(string_A)

for b in range(10):
    print(string_B)

for x in range(9):
    print((x+1)*'x')
    
for ox in range(1,10):
    if ox %2 == 0:
        print(ox*"x")
    else:
        print(ox*"o")
