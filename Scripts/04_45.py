helloMessage='Hello %s!'
print(helloMessage % ('Kate'))
print(helloMessage % ('Chris'))
helloMessage1='Hello {0:s}!'
print(helloMessage1.format('Kate'))
print(helloMessage1.format('Chris'))
helloMessage2='%s has %d %s'
print(helloMessage2 %('Kate',1,'animal'))
helloMessage3='{0:s} has {1:d} {2:s}'
print(helloMessage3.format('Kate',1,'animal'))
print(helloMessage3.format('Chris',10000,'$'))
line='{0:20s}costs{1:6d} euro;'
print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAI',6))
