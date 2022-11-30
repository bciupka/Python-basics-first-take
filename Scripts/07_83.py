numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i=0
max = len(numbers)-2
while i<max:
    print(numbers[i],numbers[i+1],numbers[i+2])
    if numbers[i+1]==numbers[i]**2 and numbers[i+2]==numbers[i+1]**2:
        print('\tFound',numbers[i]**2,numbers[i+1],'and',numbers[i+1]**2,numbers[i+2])
    i+=1


x=0
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
top = len(texts)-1
while x<top:
    if len(texts[x])==len(texts[x+1]):
        print(texts[x],texts[x+1])
    x+=1
    
