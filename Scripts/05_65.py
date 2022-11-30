marketing = ['loyality program','client promotion','market research']
print(marketing)
marketing.append('public relations')
print(marketing)
print(marketing[2])
marketing.insert(1, 'investor relations')
print(marketing)
emailMarketing=marketing.copy()
emailMarketing.sort()
print(emailMarketing)
internalEmails = 'internal communication'
emailMarketing.append(internalEmails)
print(emailMarketing)
tuple = tuple(emailMarketing)
print(tuple)



