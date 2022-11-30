number = 1
previousNumber = 0
while number<50:
    print(number+previousNumber)
    previousNumber = number
    number+=1


import random
myNumber = random.randint(0, 20)

guess = -1
trials = 0
print('Zgaduj zgadula. Od 0 do 20')
while guess != myNumber:
    guess = int(input())
    trials += 1
    if guess < myNumber:
        print('Wiecej')
    elif guess > myNumber:
        print ('Mniej')
    else:
        print('Brawo, liczba prob:',trials)
        

