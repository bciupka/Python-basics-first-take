import os

line = input('Ile max za kurs? ')

path = input('Ścieżka: ')

try:
    with open(path+r'\xd.txt', 'w') as file:
        file.write(line)
    value = int(line)
    print('Do pliku przepisano: ', value)
except ValueError as e:
    print('Many error: ', e)
except FileNotFoundError as e:
    print('Mamy error: ', e)
except:
    print('Mamy inny error')
else:
    print('O! wszystko ok!')

