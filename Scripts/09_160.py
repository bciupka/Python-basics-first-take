import datetime as dt

def sylwester(*date):
    i=0
    while i < len(date):
        
    
        today = dt.date(date[i], date[i+1], date[i+2])
        end = dt.date(date[i], 12, 31)

        delta = end - today
        print(date[i], date[i+1], date[i+2], '\t' ,delta.days, 'days')
        i+=3
        
    return

sylwester(2020, 11, 14, 2017, 4, 15, 2020, 9, 14)




def PrintAnimal(*animal):
    for i in animal:
        if i == 'cat':   
            txt = r'''
        |\---/|
        | o_o |
         \_^_/'''
            print(txt)
        elif i == 'bear':
            txt = r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''
            print(txt)
        elif i == 'bat':
            txt = r'''
           /\                 /\
          / \'._   (\_/)   _.'/ \
         /_.''._'--('.')--'_.''._\
         | \_ / `;=/ " \=;` \ _/ |
          \/ `\__|`\___/`|__/`  \/
                  \(/|\)/  
             '''
            print(txt)
        else:
            print('złe zwierze')
    return


good = PrintAnimal('cat', 'srat', 'bear', 'bat')

from datetime import date

def DaysToEndOfYear(*dates):
 
    for date_today in dates:
        
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)
 
DaysToEndOfYear(date(1999,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15),date.today())
