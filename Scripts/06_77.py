musclePain = True
fever = False
weakness = True

print('suspision of influenza' if musclePain and fever and weakness else 'The flu is unlikely')

if musclePain and fever and weakness:
    print('suspision of influenza')
elif weakness and (fever or musclePain):
    print('Just take a rest')
else:
    print('you may be cold')
    
    
isMan = False

if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print('suspision of influenza')
elif weakness and (fever or musclePain):
    print('Just take a rest')
else:
    print('you may be cold')


check = False

print('OK' if check else 'NOK')
