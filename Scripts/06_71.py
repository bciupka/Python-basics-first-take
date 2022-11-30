likes=700
shares=100

if likes>=500 and shares>=100:
    print("Obniżka!!!")
else:
    print('Nie dzisiaj :(')


isPizza = False
isDrink = True
isWeekend = False

if (isPizza or isDrink) and not isWeekend:
    print('Burger!!!')
else:
    print('Kupuj dalej :)')


diskSpace = 1000
usedSpace = 400
fileSize = 599

if diskSpace-usedSpace >= fileSize:
    print('You can download this file')
else:
    print('No! no! no!')
    
