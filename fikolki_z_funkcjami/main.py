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


#79.Stworz funkcje ktora bedzie drukowala na konsoli dane otrzymane przez pierwszy argument
# obrobione uprzednio przez wyrazenie lambda podane jako drugi argument.
