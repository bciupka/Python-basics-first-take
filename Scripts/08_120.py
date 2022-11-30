import random
import string

for i in range(10):
    print(random.randint(1,100))

number1 = random.randrange(1,101)
print(number1,'\n')
i = 0

##while number1 != number2:

while True:
    temp = random.randrange(1,101)
    i += 1
    print(temp, i)
    if temp == number1:
        break


countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

##groupNumber =  0
##temp = 1
##random.shuffle(countries)
##
##for i in countries:
##    print(i)
##    if temp % 4 == 0:
##        groupNumber += 1
##        if groupNumber == 1:
##            print('-----Grupa A-----')
##        elif groupNumber == 2:
##            print('-----Grupa B-----')
##        elif groupNumber == 3:
##            print('-----Grupa C-----')
##        elif groupNumber == 4:
##            print('-----Grupa D-----')
##        elif groupNumber == 5:
##            print('-----Grupa E-----')
##        elif groupNumber == 6:
##            print('-----Grupa F-----')
##        elif groupNumber == 7:
##            print('-----Grupa G-----')
##        elif groupNumber == 8:
##            print('-----Grupa H-----')
##    temp += 1

groupLetter =  list(string.ascii_uppercase)
random.shuffle(countries)

for i in range(len(countries)):
    if i % 4 == 0:
        print('-----Grupa %s-----' % groupLetter[i // 4])
    print(countries[i])
    

