szoveg = input('szöveg: ')
# c = 0
# for b in szoveg:
#     if b == ' ': c += 1
# if len(szoveg) == 0: print('szavak száma: 0')
# else: print(f'szavak száma: {c + 1}')¨


szavak_szama = 0
for i in range(len(szoveg) - 1):
    if szoveg[i] == ' ' and szoveg[i + 1] != ' ':
        szavak_szama += 1

if len(szoveg) != 0 and szoveg[0] != ' ':
    szavak_szama += 1 

print(f'{szavak_szama} szó')
