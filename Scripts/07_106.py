initialCapital = 20000
percent = 0.03
maxTimeYears = 10

earnings = 0
actualCapital = initialCapital
print('Ilość pieniędzy przed wpłatą:', initialCapital)
i = 1

while i <= maxTimeYears:
    earnings = percent * actualCapital
    actualCapital += earnings
    print('Ilość pieniędzy po %d lat: %d zł' % (i, actualCapital))
    i += 1
print('Ilość zarobionych pieniędzy:', round(actualCapital - initialCapital, 2), 'zł')


##liczba = 20730906
##
##string = str(liczba)
##
##lista = []
##
##lista.extend(string)
##
##y = 0
##
##for i in lista:
##    lista[y] = int(i)
##    y += 1
##print(sum(lista))

##liczba = 20730906
##
##string = str(liczba)
##
##lista = []
##
##lista.extend(string)
##
##y = 0
##
##for i in lista:
##    x = int(i)
##    y += x
##print(y)


##liczba = 20730906
##
##string = str(liczba)
##
##lista = []
##
##lista.extend(string)
##
##y = 0
##
##while y < len(lista):
##    lista[y] = int(lista[y])
##    y += 1
##print(sum(lista))



liczba = 20730906

x=0


while liczba != 0:
    x += (liczba%10)
    liczba = liczba // 10
print(x)



text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''

lista1 = text.replace('\n',' ').split()

short = []
long = []
limit = 6
i= 0

while i < len(lista1):
    if len(lista1[i]) <= limit:
        short.append(lista1[i])
        i += 1
    else:
        long.append(lista1[i])
        i += 1
print(len(long))
print(len(short))
print(len(lista1))
print(lista1)





##initialCapital = 20000
##percent = 0.03
##maxTimeYears = 10
##year=0
##capital=initialCapital
##while year<maxTimeYears:
##    year+=1
##    capital=round((1+percent)*capital,2)
##    print('after this year:', year,  'you will have:',capital)
##else:
##    print('the total revenue is', capital-initialCapital)
##print('-------------------------------------------------------')
## 
## 
##number=20730906
##tmpnumber = number
##sumOfDigits = 0
##while tmpnumber >0:
##    digit = tmpnumber % 10
##    sumOfDigits += digit
##    tmpnumber = tmpnumber//10
##else:
##    print('the sum of digits of ', number, ' is',sumOfDigits)
##print('-------------------------------------------------------')
## 
## 
##text = '''
##United Space Alliance: This company provides major support to NASA for
##various projects, such as the space shuttle. One of its projects is to
##create Workflow Automation System (WAS), an application designed to
##manage NASA and other third-party projects. The setup uses a central
##Oracle database as a repository for information. Python was chosen over
##languages such as Java and C++ because it provides dynamic typing and
##pseudo-code–like syntax and it has an interpreter. The result is that
##the application is developed faster, and unit testing each piece is easier.
##'''
##listOfWords = text.replace('\n',' ').split(' ')
##wordLength = 6
##i=0
##shortWords = 0
##longWords = 0
##while i< len(listOfWords):
##    if len(listOfWords[i])>wordLength:
##        longWords+=1
##    else:
##        shortWords+=1
##    
##    i+=1
##print("Words shorter than ",wordLength,":",shortWords)
##print("Words longer than ",wordLength,":",longWords)
##print(len(listOfWords))
##   
