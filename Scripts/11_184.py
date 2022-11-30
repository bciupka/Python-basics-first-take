import sys

file_path = r'D:\Projekty\Python\Scripts\10_pliki\temp\data_input\orders.csv'
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
          

            print('Order from drugstore "{2:s}", item "{1:s}", amount {0:d}'.format(amount, item, pharmacy_name))
        except ValueError as e:
            print('Nie powiodła się konwersja danych w 3 kolumnie w zamówieniu: ', line, '\tDodatkowe info: ', e)
        except IndexError as e:
            print('Zanówienie ma za mało danych: ', line, '\tDodatkowe info: ', e)
        except:
            print('Zepsuło się coś dziwnego: ', sys.exc_info()[0:2])


print("Processing finished")
