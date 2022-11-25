# import time
#
#
# def mierz_czas(fun):
#     def wewnetrzna(*args,**kwargs):
#         poczatek=time.time()
#         fun()
#         koniec=time.time()
#         print(f'czas trwania {koniec-poczatek}s')
#     return wewnetrzna
#
# @mierz_czas
# def zamul():
#     time.sleep(5)
#     print('koniec')
#
# zamul()

# def funkcja():
#     print('cośtam')
#
# def odpalacz(fun):
#     print(f'odpalanie funkcji {fun.__name__}')
#     fun()
#
# odpalacz(funkcja)

#78. Stwórz dwie funkcje - jedna ma zwracać powiększony tekst który otrzyma przez argument,
# druga analogicznie ale pomniejszony. Dodaj funkcję która będzie w stanie przyjąć przez argument
# inną funkcję oraz ciąg tekstowy do obróbki który następnie po obrobieniu przez funkcję podaną
# jako argument zostanie wyświetlony na konsoli

# def powieksz(tekst):
#     return tekst.upper()
#
# def pomniejsz(tekst):
#     return tekst.lower()
#
# def odpal(fun,tekst):
#     print(fun(tekst))
#
# tekst='siała BABA mak'
# odpal(powieksz,tekst)
# odpal(pomniejsz,tekst)



# def odpal(fun,tekst):
#     print(fun(tekst))
#
# tekst='siała BABA mak'
# odpal(lambda x:x.upper(),tekst)
# odpal(lambda x:x.lower(),tekst)
#
# def funkcja(x,y):
#     pass
#
# def funkcja(*args):
#     for a in args:
#         print(a)
#
# funkcja('koza',1,'costam')

#
# def opakowanie(fun,*args):
#     fun(*args)
#
# def whatever(*args):
#     for a in args:
#         print(a)
#
# opakowanie(whatever,'siema','tu','mapet')

# def whatever(**kwargs):
#     for k in kwargs:
#         print(k,kwargs[k])
#
# def opakowanie(fun,**kwargs):
#     fun(**kwargs)
#
# opakowanie(whatever,arg1='coś',arg2='coś')
#

#79. Stwórz funkcję "parse" która będzie otrzymywała przez argumenty wartosc tekstową oraz *args funkcji.
# Funkcja ta ma zastosować każdą z otrzymanych przez *args funkcji na wartości tekstowej
# którą następnie wypisze na konsoli. Dodaj funkcję "powieksz" i "podziel"
# które mają zwracać otrzymane przez argument dane odpowiednio po powiększeniu i podzieleniu
# tekstu na słowa. Wywołaj funkcję "parse" przekazując do niej ciąg tekstowy składający się z więcej
# niż 1 słowa oraz funkcje "powieksz" i "podziel"

# def powieksz(tekst):
#     return tekst.upper()
#
# def podziel(tekst):
#     return tekst.split()
#
# tekst="siała baba mak"
#
# def parse(tekst,*funcs):
#     for f in funcs:
#         tekst=f(tekst)
#     print(tekst)

#parse(tekst,lambda x:x.upper(),podziel)
#parse(tekst,podziel,powieksz)#fuuuuuu

#przerwa do 10:24

# def nadfunkcja():
#     def podfunkcja():
#         print('dupa')
#     podfunkcja()
#
# nadfunkcja()

#
# def nadfunkcja():
#     def podfunkcja():
#         print('dupa')
#     return podfunkcja
#
# f=nadfunkcja()
# f()

#80. Stwórz funcję która będzie posiadała dwie funkcje wewnętrzne.
# Jedna z tych funkcji ma powiekszac i zwracac otrzymany ciag znakow, druga pomniejszac i zwracac otrzymany ciąg znaków.
# Funkcja zewnętrzna ma zwracać funkcję powiększającą gdy zostanie jej przez argument przekazana wartosc 1 i
# funkcję pomniejszającą gdy otrzyma wartość 2. Odbierz obiekt funkcji wewnętrznej poprzez wywołanie funkcji zewnętrznej
# i zastosuj otrzymaną funkcję na ciągu tekstowym.

#
# def zewnetrzna(numerek):
#     def powieksz(tekst):
#         return tekst.upper()
#     def pomniejsz(tekst):
#         return tekst.lower()
#     if numerek==1:
#         return powieksz
#     elif numerek==2:
#         return pomniejsz
#     else:
#         raise NotImplemented()
#
# tekst="siala BABA mak"
# f=zewnetrzna(1)
# print(f(tekst))
# f=zewnetrzna(2)
# print(f(tekst))

#lista=[1,2,3]
#print(sum(lista),max(lista),min(lista),sum(lista)/len(lista))

#81. Stwórz funkcję która wydrukuje na konsoli sumę wartości przekazanych do niej jako *args

#funkcja(1,2,3,4)
#
# def funkcja(*args):
#     print(sum(args))
#
# funkcja(1,2,3,4,5)

#82. Stwórz funkcję która przyjmie nieokreśloną liczbę elementów przez argument,
# a następnie wypisze na konsoli ilość otrzymanych elementów.
# Poniżej informacji o ilości otrzymanych elementów wyświetl w osobnych liniach każdy argument oraz jego typ.
#
# def funkcja(*params):
#     print(f'ilość={len(params)}')
#     for p in params:
#         print(p)
#
#
# funkcja('coś',1111,['whatever','lubie pierogi'])

# def funkcja(x,*args):
#     pass
#
#
# def funkcja(*args,x):
#     pass
#
# funkcja(1,2,3)

#83. Stwórz funkcję która przyjmie przez argument mnożnik oraz elementy typu args.
# Funkcja ma dla kazdego elementu typu args wyswietlic na konsoli wynik jego mnożenia przez mnożnik
