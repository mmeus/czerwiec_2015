slownik = {w.split()[0]: w.split()[1] for w in open('cyfra_kodkreskowy.txt').readlines()[1:]}
kody = [w.strip() for w in open('kody.txt').readlines()]

#6.1
#parzyste = [sum(map(int, list(k[1::2]))) for k in kody]
nieparzyste = [sum(map(int, list(k[::2]))) for k in kody]

parzyste = []
for k in kody:
    parzyste.append(int(k[1]) + int(k[3]) + int(k[5]))

cyfry_kontrolne = []

'''for i in range(len(parzyste)):
    ...'''

#6.2
for p, n in zip(parzyste, nieparzyste):
    cyfry_kontrolne.append((10 - ((3 * p + n) % 10)) % 10)

for ck in cyfry_kontrolne:
    print(ck, slownik[str(ck)])

plik_kody2 = open('kody2.txt', 'w+')

#plik_kody2.write('\n'.join([f'{ck} {slownik[str(ck)]}' for ck in cyfry_kontrolne]))

for ck in cyfry_kontrolne:
    plik_kody2.write(f'{ck} {slownik[str(ck)]}\n')

#6.3
kody_kreskowe = []

for i in range(len(kody)):
    kod = '11011010' #start
    for j in kody[i]:
        kod += slownik[j] #odpowiedniki cyfr w slowniku
    kod += slownik[str(cyfry_kontrolne[i])] #cyfra kontrolna
    kod += '11010110' #stop
    kody_kreskowe.append(kod)

print(kody_kreskowe)