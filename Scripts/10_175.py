import os
import datetime

file_path = r'D:\Projekty\Python\Scripts\10_pliki\temp\data_input\test.csv'


with open(file_path, 'r') as file:
    lines = file.readlines()
i=0
while i < len(lines):
    lines[i] = lines[i].removesuffix('\n')
    if len(lines[i].split(',')) == 3:
        print('Order from drugstore "{0:s}", item "{1:s}", amount {2:s}\n'.format(lines[i].split(',')[0],lines[i].split(',')[1],lines[i].split(',')[2]))
    else:
        print('Line "%s\" malformed!!!\n' % lines[i])
    i+=1
print("Processing finished")


##with open(file_path,"r") as file:
## 
##    for line in file:
## 
##        line = line.replace('\n','')
##        order = line.split(',')
## 
##        if len(order) == 3:
##            print('Order from drugstore "%s", item "%s", amount %s' %
##                  (order[0],order[1],order[2]))
##        else:
##            print("Line %s malformed!!!" % line)
## 
##print("Processing finished")


##file = open(file_path, 'r')
##
##content = file.read()
##print(content)
##file.close()
##
##with open(file_path, 'r') as file1:
##    content1 = file1.read()
##    print(content1)
##
##
##with open(file_path, 'r') as file2:
##    for i in file2:
##        print(i)
##
##file3 = open(file_path, 'r')
##
##for i in file3:
##    print(i)
##file3.close()
##        
##with open(file_path, 'r') as file4:
##    print(file4.readlines())
##
##with open(file_path, 'r') as file5:
##    print(file5.read(10))
