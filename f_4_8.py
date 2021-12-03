mondat = input('mondat: ')

if len(mondat) == 0:
    print('nem is írtál be semmit')
elif mondat[len(mondat) - 1] == '!':
    print('felkiáltó/felszólító/óhajtó mondat')
elif mondat[len(mondat) - 1] == '?':
    print('kérdő mondat')
elif mondat[len(mondat) - 1] == '.':
    print('kijelentő mondat')
else:
    print('nem lehet eldönteni')