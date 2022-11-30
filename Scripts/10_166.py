def check_int(s):
#sprawdzenie czy jest decimal (bez znaku)
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()



astr = input('Podaj a: ')
bstr = input('Podaj b: ')
cstr = input('Podaj c: ')

##if not( check_int(a_str) and check_int(b_str) and check_int(c_str) ):

if not check_int(astr) or not check_int(bstr) or not check_int(cstr):
    print('Podaj liczby całkowite')
else:
    a = int(astr)
    b = int(bstr)
    c = int(cstr)
    if a == 0:
        print('To nie równanie kwadratowe')
    else:
        delta = b**2 - 4*a*c
        if delta <0:
            print('Brak rozwiązań')
        elif delta == 0:
            x = -b/(2*a)
            print('Rozwiązanie: ', x)
        elif delta > 0:
            x = (-b-delta**(1/2))/(2*a)
            x1 = (-b+delta**(1/2))/(2*a)
            print('Rozwiązania: ', x, x1)


             
