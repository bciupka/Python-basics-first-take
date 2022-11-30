import math

def GiveGeomSeqElement(a1=2, factor=2, index=2):
    a = []
    a.append(a1)
    i=0
    while i < index-1:
        an = a[i]*factor
        a.append(an)
        i+=1
    print(a[index-1])
    return

GiveGeomSeqElement(1, 2, 64)

##def GiveGeomSeqElement(a1=2,factor=2,index=2):
##    #returns n-th term of geometric sequence starting with element a1 and having 
##    value = a1*pow(factor,index-1)
##    return value
##print('element 64 =',GiveGeomSeqElement(1,2,64))
##print('------------------------------------------------')


def GiveGeomSeqElementAll(a1=2, factor=2, index=2):
    a = []
    a.append(a1)
    i=0
    print(i+1, '\t', a[i])
    while i < index-1:
        an = a[i]*factor
        a.append(an)
        print(i+2, '\t', a[i+1])
        i+=1
    return

GiveGeomSeqElementAll(1, 2, 10)


def GiveFactorForGeomSeq(an, an1):
    q = an1/an
    print(q)
    return


GiveFactorForGeomSeq(12, 24)

##def GiveSumOfNElementsGeomSeq(a1=2, factor=2, index=2):
##    a = []
##    a.append(a1)
##    i=0
##    while i < index-1:
##        an = a[i]*factor
##        a.append(an)
##        i+=1
##    print(sum(a))
##    return
##
##GiveSumOfNElementsGeomSeq(2, 3, 4)

def GiveSumOfNElementsGeomSeq(a1=2, factor=2, index=2):
    suma = (a1*(1-factor**index))/(1-factor)
    print(suma)
    return

GiveSumOfNElementsGeomSeq(2, 3, 4)

