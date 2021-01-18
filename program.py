n=int(input('Podaj wielkosc tablicy:'))
tab=[0]*n
i=0
while i<n:
    tab[i]=int(input('Podaj liczbe:'))
    i+=1
print(tab)
suma=0
srednia=0
licz=0
ind=n-1
j=0
for j in tab:
    if j>tab[ind]:
        licz+=1
        suma+=j
        srednia=suma/licz
print(suma)
print(srednia)