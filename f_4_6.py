szoveg = input('szöveg: ')

# e_betuk_szama = 0
# for b in szoveg:
#     if b == 'e' or b == 'E':
#         e_betuk_szama += 1
# sz = szoveg.count('e') + szoveg.count('E')
# print(e_betuk_szama)
# print(sz)

c = 0
for b in szoveg:
    if b in 'eE':
        c += 1