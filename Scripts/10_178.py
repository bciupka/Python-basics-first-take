import os

##webaddresses = []
##line = input("Wprowadź adres: ")
##
##while len(line) !=0:
##    webaddresses.append(line)
##    line = []
##    line = input("Wprowadź adres: ")
##
##dirname = r'D:\Projekty\Python\Scripts\10_pliki\temp\data_output'
##
##filename = input("Wprowadź nazwę pliku: ")+'.txt'
##
##filepath = os.path.join(dirname, filename)
##
##with open(filepath, 'w') as file:
##    for i in webaddresses:
##        file.write(i+'\n')


file_path = input('Podaj ścieżke: ')

while not os.path.isfile(file_path):
    file_path = input('Plik nie istnieje\nPodaj ścieżke: ')

webaddresses = []

with open(file_path, 'r') as file:
    for i in file.readlines(): ## in file:
        webaddresses.append(i.removesuffix('\n'))

for i in webaddresses:
    if i.find('.pl') == -1: ##line.endswith('.pl'):
        print('Adres '+i+' nie jest z pOLSKI')
        end = '\webs_others.txt'
    else:
        print('Adres '+i+' jest z pOLSKI')
        end = '\webs_pl.txt'
    dirname = os.path.dirname(file_path) + end
    with open(dirname, 'a') as wfile:
        wfile.write(i+'\n')

##dirname = os.path.dirname(file_path)
##
##filePL = open(dirname+'\webs_pl2.txt', 'a')
##fileOthers = open(dirname+'\webs_others2.txt', 'a')
##
##for i in webaddresses:
##    if i.find('.pl') == -1: ##line.endswith('.pl'):
##        print('Adres '+i+' nie jest z pOLSKI')
##        fileOthers.write(i+'\n')
##    else:
##        print('Adres '+i+' jest z pOLSKI')
##        filePL.write(i+'\n')
##
##filePL.close()
##fileOthers.close()
##    
