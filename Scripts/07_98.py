i=10
x=1


for silnia in range(i):
    x=x*(silnia+1)
    if silnia == i-1:
        print(x)


y=1

for iteracja in range(i):
    y=y*(iteracja+1)
    print(y)
        

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for z in list_noun:
    for v in list_adj:
        print(z, v)


x2=1

for silnia2 in range(1,i+1):
    x2 *= silnia2
print(x2)

y2 = 1

for iteracja2 in range(1,i+1):
    for silnia3 in range(1,iteracja2+1):
        y2 *= silnia3
    print(y2)
    y2=1
