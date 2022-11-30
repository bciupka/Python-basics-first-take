likes=600
shares=10

if likes < 500:
    print('Nie ma lajków :(')
else:
    if shares < 100:
        print('Nie ma shareów')
    else:
        print('Obniżka!!!')

if likes < 500:
    print('Nie ma lajków :(')
elif shares < 100:
    print('Nie ma shareów')
else:
    print('Obniżka!!!')



isPizza = False
isDrink = False
isWeekend = False

if (isPizza or isDrink) and not isWeekend:
    print('Burger!!!')
elif isPizza and isDrink:
    print('Kupiłeś pizze i napój ale jest weekend :(')
elif isPizza:
    print('Kupiłeś pizze ale jest weekend :(')
elif isDrink:
    print('Kupiłeś napój ale jest weekend :(')
elif not isWeekend:
    print('Nie kupiłes ani pizy ani napoju a nie ma weekendu. Co Ty wyrabiasz?')
else:
    print('Nie kupiłes ani pizy ani napoju a w dodatku mamy weekend :( Zapraszamy pnownie !!!')

