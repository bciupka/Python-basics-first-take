import datetime as dt

def sylwester(year=dt.date.today().year,
              month=dt.date.today().month,
              day=dt.date.today().day):
    


    today = dt.date(year, month, day)
    end = dt.date(year, 12, 31)

    delta = end - today

    return delta.days

dni = sylwester(2020, 11, 14)
print(dni, 'days')
dni = sylwester()
print(dni, 'days')



def PrintAnimal(animal=''):
    if animal == 'cat':   
        txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
        print(txt)
        good=True

    elif animal == 'bear':
        txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
        print(txt)
        good=True
    elif animal == 'bat':
        txt = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/  
         '''
        print(txt)
        good=True
    else:
        print('złe zwierze')
        good=False
    return good


good = PrintAnimal('cat')
print('okok' if good else 'noknok')
good = PrintAnimal('bat')
print('okok' if good else 'noknok')
good = PrintAnimal('dog')
print('okok' if good else 'noknok')
good = PrintAnimal()
print('okok' if good else 'noknok')
