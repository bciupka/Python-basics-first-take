import os
import time

folder = input('Podaj ścieżkę: ')


if not os.path.isdir(folder):
    print('To nie katalog')
else:
    file = input('Podaj plik: ')
    path = os.path.join(folder, file)
    if not os.path.isfile(path):
        print('To nie plik')
    else:
        print('Właściwości pliku', os.path.basename(path))
        print('Ostatnia data modyfikacji: ', time.strftime('%a, %d, %b, %Y, %H, %M, %S', time.localtime(os.path.getmtime(path))))
        print('Rozmiar: ', os.path.getsize(path),'B')
        print('Bieżący katalog: ', os.getcwd())
        print('Ścieżka względna: ', os.path.relpath(path))
