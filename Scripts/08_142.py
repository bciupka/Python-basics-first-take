colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for i in colors:
    for i2 in figures:
        aCard = i2.copy()
##        aCard['Color'] = i
        aCard.update({'Color':i})
        allCards.append(aCard)

print(allCards, 3*'\n')


import random as rd

rd.shuffle(allCards)

print(allCards, 3*'\n')


player1 = []
player2 = []

for i in allCards:
    if allCards.index(i) % 2 == 0:
        player1.append(i)
    else:
        player2.append(i)

        
print(player1, 3*'\n')
print(player2, 3*'\n')


while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print('Gracz 1: %s, Gracz 2: %s, Wygrywa gracz 1' % (card1['Figure']+' of '+card1['Color'], card2['Figure']+' of '+card2['Color']), len(player1)*'*')
    elif card2['Power'] > card1['Power']:
        player2.append(card1)
        player2.append(card2)
        print('Gracz 1: %s, Gracz 2: %s, Wygrywa gracz 2' % (card1['Figure']+' of '+card1['Color'], card2['Figure']+' of '+card2['Color']), len(player2)*'*')
    else:
        war = []
        while len(player1)-1 > 0 and len(player2)-1 > 0:
            war.append(card1)
            war.append(card2)
            war.append(player1.pop(0))
            war.append(player2.pop(0))
            card1 = player1.pop(0)
            card2 = player2.pop(0)
            if card1['Power'] > card2['Power']:
                player1.append(card1)
                player1.append(card2)
                player1.extend(war)
                print('Gracz 1: %s, Gracz 2: %s, Wojne wygrywa gracz 1' % (card1['Figure']+' of '+card1['Color'], card2['Figure']+' of '+card2['Color']), len(player1)*'*')
                break
            elif card2['Power'] > card1['Power']:
                player2.append(card1)
                player2.append(card2)
                player2.extend(war)
                print('Gracz 1: %s, Gracz 2: %s, Wojne wygrywa gracz 2' % (card1['Figure']+' of '+card1['Color'], card2['Figure']+' of '+card2['Color']), len(player2)*'*')
                break
            else:
                print('Gracz 1: %s, Gracz 2: %s, Brak rozstrzygnięcia wojny' % (card1['Figure']+' of '+card1['Color'], card2['Figure']+' of '+card2['Color']), len(player1)*'*', len(player2)*'*')
                continue
            break
                

            

print('Wygrał gracz 2' if len(player1)<len(player2) else 'Wygrał gracz 1')
   
