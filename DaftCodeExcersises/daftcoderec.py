pion = 8
starypion = 8
poziom = 8
starypoziom = 8
zakres = 9
cykle = 4
cykletestowy = 0
# jeden cykl ,niej zmniejsza ilosc koniecnzych ruchów o 2


#ilosc cykli jako zmienna która mówi o ile przesunąć orbienie pierścienia so środka


pentla = [[1]*zakres for n in range(zakres)]
pentla[8][8] = zakres*zakres

while cykletestowy != 4:
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

prawaprzekatna = zakres
sumaprawejprzekatnej = 0

for numernowegopoziomu, nowypoziom in enumerate(pentla):
    print ("otonowypoziom",numernowegopoziomu, nowypoziom)
    for numernowegopionu, nowypion in enumerate(nowypoziom):
        print(nowypion)
        if numernowegopionu == numernowegopoziomu:
            sumaprawejprzekatnej = sumaprawejprzekatnej + pentla[numernowegopoziomu][numernowegopionu]
            print("TO DODAMY", pentla[numernowegopoziomu][numernowegopionu])

print("sumaprawejprzekatnej", sumaprawejprzekatnej)


lewaprzekatna = zakres
sumalewejprzekatnej = 0
przesuniecielewejzmiennej = 1

for numernowegopoziomulewo, nowypoziomlewo in enumerate(pentla):
    print(nowypoziomlewo)
    # print ("otonowypoziom",numernowegopoziomulewo, nowypoziomlewo)
    # print(len(nowypoziomlewo))
    # for numernowegopionulewo, nowypionlewo in enumerate(nowypoziomlewo):
    # print(pentla[numernowegopoziomulewo][len(nowypoziomlewo)-przesuniecielewejzmiennej])

    sumalewejprzekatnej = sumalewejprzekatnej + pentla[numernowegopoziomulewo][(len(nowypoziomlewo))-przesuniecielewejzmiennej]
    print (pentla[numernowegopoziomulewo][(len(nowypoziomlewo))-przesuniecielewejzmiennej])
    if przesuniecielewejzmiennej != lewaprzekatna:
        przesuniecielewejzmiennej = przesuniecielewejzmiennej +1
print(sumalewejprzekatnej)

print("prawa", sumaprawejprzekatnej)
print("lewo", sumalewejprzekatnej)

print ("suma", sumalewejprzekatnej + sumaprawejprzekatnej)




# def diags(mat):
#     width, height = len(mat[0]), len(mat)
#     def diag(sx, sy):
#         for x, y in zip(range(sx, height), range(sy, width)):
#             yield mat[x][y]
#     for sx in range(height):
#         yield list(diag(sx, 0))
#     for sy in range(1, width):
#         yield list(diag(0, sy))
#
# print (list(diags(pentla)))
