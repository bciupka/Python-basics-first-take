import math

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

print(len(inputdata), len(factortable))


if len(inputdata) == len(factortable):
    for i in range(len(inputdata)):
        minValue = inputdata[i] - factortable[i]*inputdata[i]
        maxValue = inputdata[i] + factortable[i]*inputdata[i]
        minInteger=math.floor(minValue)
        maxInteger = math.ceil(maxValue)
        print(minInteger, inputdata[i], maxInteger, sep='\t')
else:
    print("inputdata and factortable need to have equal number of elements")


    
import random

for i in range(len(inputdata)):
    minValue = inputdata[i] - random.randint(0,1) * inputdata[i]
    maxValue = inputdata[i] + random.randint(0,1) * inputdata[i]
    print(i+1, minValue, maxValue, sep='\t')


import datetime

print(datetime.date.today())
print(datetime.date.today().strftime('%Y %m %d'))
