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
#
# def funkcja(mnoznik,*elementy):
#     for e in elementy:
#         print(mnoznik*e)
#
# funkcja(10,1,2,3,4)
#
# def funkcja(**kwargs):
#     for k in kwargs:
#         print(k,kwargs[k])
#
# funkcja(param1='Andrzej',param2='Klusiewicz',costam='Mapet')

#84. Stworz funkcje "config" ktora bedzie otrzymywala argumenty kwargs bedace ustawieniami.
# Funkcja ta ma zapisac podane argumenty do pliku config.csv w 2 kolumnach
# z czego pierwsza jest nazwa argumentu a druga jego wartoscia.
# Jesli dane argument juz istnieje w pliku to trzeba bedzie
# tylko zaktualizowac jego wartosc, jesli jeszcze go nie ma to trzeba go bedzie dodac do pliku.

#
# def config(**kwargs):
#     sl=dict()
#     for e in [e.strip().split('=') for e in open('config.conf',encoding='utf-8')]:
#         #print(e)
#         sl[e[0]]=e[1]
#     for k in kwargs:
#         sl[k]=kwargs[k]
#     with open('config.conf',encoding='utf-8',mode='w') as plik:
#         for k in sl:
#             plik.write(f'{k}={sl[k]}\n')
#
#
# config(encoding='windows-1250',color='black')

# @dekorator

# def funkcja():
#     print('coś!')
#
# def dekorator(fun):
#     def wewnetrzna():
#         print('przed')
#         fun()
#         print('po')
#     return wewnetrzna
#
# f=dekorator(funkcja)
# f()

#
# def dekorator(fun):
#     def wewnetrzna():
#         print('przed')
#         fun()
#         print('po')
#     return wewnetrzna
#
# @dekorator
# def funkcja():
#     print('coś!')
#
# funkcja()
#
# f=dekorator(funkcja)
# f()

#85. Stwórz funkcję której zadaniem będzie poczekanie 3 sekundy i wypisanie na konsoli komunikatu.
# Dodaj dekorator który zliczy czas wykonywania tej funkcji. Pobranie aktualnego czasu to: "time.time()",
# wstrzymanie na 3 sekundy: "time.sleep(3)"
#
# import time
# def czekacz():
#     time.sleep(3)
#     print('już koniec :(')
#
# def dekorator(fun):
#     def wewnetrzna():
#         p=time.time()
#         fun()
#         k=time.time()
#         print(f'czas trwania: {k-p}s')
#     return wewnetrzna
#
#
# udekorowana=dekorator(czekacz)
# udekorowana()

# import time
# p=time.time()
# time.sleep(1)
# k=time.time()
# print(f'{k-p}s')


#
# import time
#
# def dekorator(fun):
#     def wewnetrzna():
#         p=time.time()
#         fun()
#         k=time.time()
#         print(f'czas trwania: {k-p}s')
#     return wewnetrzna
#
# @dekorator()
# def czekacz():
#     time.sleep(3)
#     print('już koniec :(')
#
# czekacz()


#przerwa do 11:39
#
# def dekorator(fun):
#     def wewnetrzna():
#         print('przed')
#         fun()
#         print('po')
#     return wewnetrzna
# def jakas(x):
#     for i in range(1,x+1):
#         print(f'jakaś po raz {i}')
#
# f=dekorator(jakas)
# f()

#
# def dekorator_1_arg(fun):
#     def wewnetrzna(param):
#         print('przed')
#         fun(param)
#         print('po')
#     return wewnetrzna
#
# def dekorator_no_args(fun):
#     def wewnetrzna():
#         print('przed')
#         fun()
#         print('po')
#     return wewnetrzna
#
#
# def jakas(x):
#     for i in range(1,x+1):
#         print(f'jakaś po raz {i}')
#
# def inna():
#     print('inna....')
#
# j=dekorator_1_arg(jakas)
# j(10)
#
# i=dekorator_no_args(inna)
# i()
#

# f=dekorator(inna)
# f()
# f=dekorator(jakas)
# f(10)


# def dekorator(fun):
#     def wewnetrzna(*args,**kwargs):
#         print('przed')
#         fun(*args,**kwargs)
#         print('po')
#     return wewnetrzna
#
#
# @dekorator
# def jakas(x):
#     for i in range(1,x+1):
#         print(f'jakaś po raz {i}')
# @dekorator
# def inna():
#     print('inna....')
#
# jakas(3)
# inna()
# #
# def dekorator(fun):
#     def wewnetrzna(*args,**kwargs):
#         print('przed')
#         x=fun(*args,**kwargs)
#         print('po')
#         return x
#     return wewnetrzna
# #
# @dekorator
# def funkcja():
#     return 'nietoperz'
#
# print(funkcja())

#86. Stwórz dekodator który będzie zawsze zaokrąglał do 2 miejsc po przecinku wynik zwracany przez dekordowaną funkcję

#SOLID - szczególnie otwarte na rozwój zamknięte na zmiany


#
# def zaokraglij(fun):
#     def wewnetrzna(*args,**kwargs):
#         return round(fun(*args,**kwargs),2)
#
#     return wewnetrzna
#
# @zaokraglij
# def funkcja1():
#     return 10/3
# @zaokraglij
# def funkcja2(x,y):
#     return x/y
#
# print(funkcja1())
# print(funkcja2(10,3))

#87.Stwórz dekorator który będzie rejestrował do pliku loga wszystkie wywołania dekorowanej
# funkcji z informacją o nazwie dekorowanej funkcji, dacie i czasie jej wywołania oraz argumentach przekazanych
# do dekorowanej funkcji. Log ma być w formacie CSV. Same argumenty powinny być rejestrowane w jednej kolumnie razem.

# Pobranie nazwy funkcji: fun.__name__,
# # Pobranie aktualnego czasu i daty:
# from datetime import datetime
# now = datetime.now()
# print(now.strftime("%d/%m/%Y %H:%M:%S"))

#@app.route('/')
# import time
# from datetime import datetime
# def loguj(fun):
#     def wewnetrzna(*args,**kwargs):
#         result=fun(*args,**kwargs)
#         now = datetime.now()
#         with open('log.txt',encoding='utf-8',mode='a') as plik:
#             plik.write(now.strftime("%d/%m/%Y %H:%M:%S")+';'+fun.__name__+";"+str(args)+str(kwargs)+";"+str(result)+"\n")
#     return wewnetrzna
#
# @loguj
# def testowa(x,y):
#     time.sleep(1)
#     print(f'x*y={x*y}')
#     return x*y
#
# @loguj
# def kolejna():
#     return "koza"
#
# testowa(3,4)
# kolejna()
#app.route('/costam')
#
# def powtorz(x):
#     def dekorator(fun):
#         def wewnetrzna(*args,**kwargs):
#             for i in range(1,x+1):
#                 fun()
#         return wewnetrzna
#     return dekorator
#
# @powtorz(10)
# def funkcja():
#     print('funkcja!')
#
# funkcja()


#88. Stwórz dekorator który będzie zwracał wynik dekorowanej funkccji zaokraglony do tylu miejsc
#po przecinku ile podamy w argumencie dekoratora

# @zaokralij(4)
# def funkcja():
#     return 10/3