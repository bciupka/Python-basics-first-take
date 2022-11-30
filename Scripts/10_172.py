import os
import datetime

data_input_catalog = r'D:\Projekty\Python\Scripts\10_pliki\temp\data_input'
data_output_catalog = r'D:\Projekty\Python\Scripts\10_pliki\temp\data_output'

today = datetime.datetime.now()

today_output_catalog = os.path.join(data_output_catalog, today.strftime('%Y-%m-%d')+'.txt')

is_input_dir = os.path.isdir(data_input_catalog)
is_output_dir = os.path.isdir(data_output_catalog)
is_today_filedir = os.path.exists(today_output_catalog)

if not is_input_dir:
    print('Input i output nie istnieja' if not is_output_dir else 'Input nie istnieje')
elif not is_output_dir:
    print('Output nie istnieje')
elif is_today_filedir:
    print('Today już istnieje (plik/katalog)')
else:
    print('Można kontynuować')


print(os.path.isfile(today_output_catalog))
print(os.path.isdir(today_output_catalog))
print(os.path.exists(today_output_catalog))
