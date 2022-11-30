import datetime as dt

def sylwester(year=dt.date.today().year,
              month=dt.date.today().month,
              day=dt.date.today().day):
    


    today = dt.date(year, month, day)
    end = dt.date(year, 12, 31)

    delta = end - today


    print(delta.days, 'days')
    return

sylwester(2020, 11, 14)
sylwester()




def PrintAnimal(animal=''):
    if animal == 'cat':   
        txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
        print(txt)

    elif animal == 'bear':
        txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
        print(txt)
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
    else:
        print('złe zwierze')
    return


PrintAnimal('cat')
PrintAnimal('bat')
PrintAnimal('dog')
PrintAnimal()
