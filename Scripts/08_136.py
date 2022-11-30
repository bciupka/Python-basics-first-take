import random

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']

allCards = []


for i in colors:
    for i2 in figures:
        allCards.append(i2+' of '+i)
print(allCards, 3*'\n')

random.shuffle(allCards)

print(allCards, 3*'\n')


player1 = []
player2 = []

allCards2 = allCards.copy()

for i in allCards:
    if allCards.index(i) % 2 == 0:
        player1.append(i)
    else:
        player2.append(i)

print(player1, 3*'\n')
print(player2, 3*'\n')

player1.clear()
player2.clear()

i = 0

while i < len(allCards2):
    if len(player1) < len(allCards2) // 2:
        player1.append(allCards[i])
        i+=1
    else:
        player2.append(allCards[i])
        i+=1


print(player1, 3*'\n')
print(player2, 3*'\n')


##player1 = allCards[:12]
##player2 = allCards[12:]
## 
## 
##print('-------PLAYER 1--------')
##print(player1)
## 
##print('-------PLAYER 2--------')
##print(player2)    
