
g=4546
Tg = int(g / 1000)
Hg = int((g % 1000) / 100)
Teg = int(((g % 1000) % 100) / 10)
Ug = int(((g % 1000) % 100) % 10)
Tn = int(g / 1000)
Hn = int((g % 1000) / 100)
Ten = int(((g % 1000) % 100) / 10)
Un = int(((g % 1000) % 100) % 10)
L = [Tg, Hg, Teg, Ug, Tn, Hn, Ten, Un]
print (L)
print (L[3])