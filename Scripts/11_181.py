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
        except:
            print('Nie dało rady', sys.exc_info()[1])

print("Processing finished")
