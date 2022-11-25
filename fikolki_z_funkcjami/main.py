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
