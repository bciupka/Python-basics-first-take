fibonacciIterations=20
x=0
y=0
z=0

for i in range(fibonacciIterations):
    if i == 0:
        print(i+1, x)
    elif i == 1:
        y = 1
        print(i+1, y)
    else:
        z=x+y
        print(i+1, z)
        y, x = z, y
        
text='''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
'''

##lista = text.replace('\n', ' ').split()
##for i1 in lista:
##    if 'p' in i1:
##        print(i1)

lista = text.replace('\n', ' ').split()
for i1 in lista:
    if i1.lower().find('p')>=0:
        print(i1)
      
      

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}

for i2 in dictionary:
    print(i2,'-',dictionary[i2])


dictio = {}

for i3 in lista:
    i3 = i3.lower().strip('.,!?:') 
    if i3 not in dictio.keys():
        dictio.setdefault(i3, 1)
    else:
        dictio.update({i3 : dictio[i3] + 1})
        
for i4 in dictio:
    print(i4,'-',dictio[i4])

    

    

