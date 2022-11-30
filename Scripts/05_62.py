hitsTitles=['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
hitsTitles.insert(2, 'HOTEL CALIFORNIA')
hitsTitles.insert(0, 'SOUND OF SILENCE')
print(hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove('HOTEL CALIFORNIA')
hitsTitles[0]= 'ENJOY THE SILENCE'
hitsToRead=hitsTitles.copy()
hitsToRead.reverse()
print(hitsToRead)
hitsToRead.sort()



print(hitsToRead.pop(0))
print(hitsToRead.pop(0))


additionalSongs=['WISH YOU WERE HERE', 'NOTHING COMPARES 2 U']

##hitsToRead=hitsToRead+additionalSongs
hitsToRead.extend(additionalSongs)
print(hitsToRead)

print(hitsTitles)

print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))

hitsToRead.clear()
print(hitsToRead)

