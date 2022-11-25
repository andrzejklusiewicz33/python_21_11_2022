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

