kisbetuk =  'abcdefghijklmnopqrstuvwxyz'
nagybetuk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

szoveg = input('szoveg:\n')

nagybetus_szoveg = ''

for b in szoveg:
    if b in kisbetuk:
        i = 0
        while kisbetuk[i] != b: i += 1
        nagybetus_szoveg += nagybetuk[i]
    else: nagybetus_szoveg += b

print('csupa nagybetűvel:')
print(nagybetus_szoveg)

kisbetus_szoveg = ''
for b in szoveg:
    if b in nagybetuk:
        i = 0
        while nagybetuk[i] != b: i += 1
        kisbetus_szoveg += kisbetuk[i]
    else: kisbetus_szoveg += b

print('csupa csupa kisbetűvel:')
print(kisbetus_szoveg)
