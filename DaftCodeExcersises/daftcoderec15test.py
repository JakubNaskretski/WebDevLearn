
h = 4

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	    return False
    return True

pion = h
starypion = h
poziom = h
starypoziom = h
zakres = h+1
cykle = 0
cykletestowy = 0
print (h)
# jeden cykl ,niej zmniejsza ilosc koniecnzych ruchów o 2


#ilosc cykli jako zmienna która mówi o ile przesunąć orbienie pierścienia so środka


pentla = [[1]*zakres for n in range(zakres)]
pentla[h][h] = zakres*zakres

while cykletestowy != ((h/2)):
# dół
    for i in range(0,zakres):
        x = pentla[poziom][pion]
        if pion != 0+cykletestowy:
            pion = pion -1
            x= x-1
        pentla[poziom][pion] = (x)
    #lewo
    for i in range(0,zakres):
        y = pentla[poziom][pion]
        if poziom != 0+cykletestowy:
            poziom = poziom -1
            y= y-1

        pentla[poziom][pion] = (y)

    #góra
    for i in range(0,zakres):
        x = pentla[poziom][pion]
        if pion != (zakres-1 - cykletestowy):
            pion = pion +1
            x= x-1
        pentla[poziom][pion] = (x)

    #dół
    for i in range(0,zakres-1):
        y = pentla[poziom][pion]
        if poziom != (zakres-2- cykletestowy):
            poziom = poziom +1
            y= y-1
        pentla[poziom][pion] = (y)
    cykletestowy = cykletestowy + 1




for i in pentla:
        print (i)
        print()


prawaprzekatna = zakres
sumaprawejprzekatnejprime = 0
for numernowegopoziomu, nowypoziom in enumerate(pentla):
    for numernowegopionu, nowypion in enumerate(nowypoziom):
        # if (pentla[numernowegopoziomu][numernowegopionu]) == 1:
        #     print ("MAMY JEDYNKE!!")
        if numernowegopionu == numernowegopoziomu:
            if is_prime_number(pentla[numernowegopoziomu][numernowegopionu]):
                # if (pentla[numernowegopoziomu][numernowegopionu]) == 1:
                    # print ("MAMY JEDYNKE!!")
                sumaprawejprzekatnejprime = sumaprawejprzekatnejprime + 1


lewaprzekatna = zakres
sumalewejprzekatnejprime = 0
przesuniecielewejzmiennej = 1
for numernowegopoziomulewo, nowypoziomlewo in enumerate(pentla):
    if is_prime_number(pentla[numernowegopoziomulewo][(len(nowypoziomlewo))-przesuniecielewejzmiennej]):
        sumalewejprzekatnejprime = sumalewejprzekatnejprime + 1
    if przesuniecielewejzmiennej != lewaprzekatna:
        przesuniecielewejzmiennej = przesuniecielewejzmiennej +1

# print("prawa", sumaprawejprzekatnejprime)
# print("lewo", sumalewejprzekatnejprime)
# print ("suma prime", sumalewejprzekatnejprime + sumaprawejprzekatnejprime)


#sumaryczna ilość liczb
prawaprzekatna = zakres
sumaprawejprzekatnej = 0

for numernowegopoziomu, nowypoziom in enumerate(pentla):
    for numernowegopionu, nowypion in enumerate(nowypoziom):
        if numernowegopionu == numernowegopoziomu:
            sumaprawejprzekatnej = sumaprawejprzekatnej + 1



lewaprzekatna = zakres
sumalewejprzekatnej = 0
przesuniecielewejzmiennej = 1

for numernowegopoziomulewo, nowypoziomlewo in enumerate(pentla):
    sumalewejprzekatnej = sumalewejprzekatnej + 1
    if przesuniecielewejzmiennej != lewaprzekatna:
        przesuniecielewejzmiennej = przesuniecielewejzmiennej +1

wynik = (sumalewejprzekatnejprime + sumaprawejprzekatnejprime)/(sumalewejprzekatnej + sumaprawejprzekatnej-1)


print("prawa sumarycznie", sumaprawejprzekatnej)
print("lewa sumarycznie", sumalewejprzekatnej)

print ("suma nie prime", sumalewejprzekatnej + sumaprawejprzekatnej-1)

print("procenty", (sumalewejprzekatnejprime + sumaprawejprzekatnejprime)/(sumalewejprzekatnej + sumaprawejprzekatnej-1))
