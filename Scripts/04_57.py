q='a gentleman'
print(q[3]+q[6:8]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8:])

x='THE MORSE CODE'
print(x[1:3]+x[6]+x[2:4]+x[10:12]+x[4]+x[2:4]+x[12]+x[5]+x[0]+x[7])

line='\'Program "Pytanie na śniadanie" nadamy o: 6:00\''

time=line[line.find(':')+2:]

print(time)

tmp=line[line.find('"')+1:]

title=tmp[:tmp.find('"')+1]

print(title,time)
