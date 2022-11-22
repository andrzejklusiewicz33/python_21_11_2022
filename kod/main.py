# dodatki:
# dekoratory
# obiektowość
# Faker
# print("hello")
# print('hello')
# print("Mc'Donalds")
# x='koza'
# print(x,type(x))
# x=10
# print(x,type(x))
# x=1.3
# print(x,type(x))
# x='nietoperz'
# print('x='+x)
# x=10
# print('x='+x)
# print('x='+str(x))
# x=10
# y=66
# print("x={} y={}".format(x,99))
# print(f'x={x} y={y}')
# jakiś komentarz
# zwierze=input('podaj nazwę zwierza:\n')
# print(f'wybrane zwierze to {zwierze}')

# x=input('podaj x:\n')
# #print(x/3)
# print(type(x))

# print('hajs '*100)

# x=int(input('podaj x:\n'))
# x=float(  input('podaj x:\n')    )
# print(type(x))
# print(x/3)

# 1. Napisz program który przyjmie od uzyszkodnika jego imie oraz nazwisko, a nastepnie
# wyswietli komunikat typu "Witaj Andrzej Klusiewicz!"
# PEP8
# import this
# first_name=input('podaj imię:\n')
# last_name=input('podaj nazwisko:\n')
# print("Witaj "+first_name+" "+last_name+"!")
# print("Witaj {} {}!".format(first_name,last_name))
# print(f'Witaj {first_name} {last_name}!')
#

# 2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika jego masę
# w kilogramach i wzrost w metrach, wyliczy i wypisze BMI.

# print(80/pow(1.76,2))
# print(round(80/pow(1.76,2),2))
# print(80/(1.76*1.76))
#
# weight=float(input('podaj masę:\n'))
# height=float(input('podaj wzrost:\n'))
# #bmi=round(weight/pow(height,2),2)
# bmi=round(weight/(height*height),2)
# print(bmi)

# przerwa do 10:23

# x=2
# if x==1:
#     print('jeden')
#     print('.....')
# print('koniec')
#
# x=2
# if x==1:
#     print('jeden')
#     print('.....')
# else:
#     print('nie jeden...')
# print('koniec')


# x=0
# if x==1:
#     print('jeden')
# elif x==2:
#     print('dwa')
# elif x==3:
#     print('trzy')
# else:
#     print('poza zakresem')
#
# if 1==1:
#     print('to jasne')
#
# print('koniec')


# 3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić
# tę wartość z informacją "wartość dodatnia", jeśli zero to wyświetlamy z informacją "równe zero",
# jeśli ujemna to wyświetlamy "wartość ujemna".
#
# def funkcja(x):
#     print(x)
#
# funkcja(input('podaj coś:\n'))
# funkcja(111111)

#
# some_number=float(input('dej liczbę:\n'))
# if some_number<0:
#     print(f'{some_number} jest ujemne')
# elif some_number>0:
#     print(f'{some_number} jest dodatnie')
# else:
#     print(f'{some_number} jest zerem')


# 4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#  wyświetlił nam również odpowiedni opis wg skali z Wikipedii.
#
# weight=float(input('podaj masę:\n'))
# height=float(input('podaj wzrost:\n'))
# bmi=round(weight/pow(height,2),2)
# print(bmi)
#
# if bmi<16:
#     print('wyglodzenie')
# elif bmi<17:
#     print('wychudzenie')
# elif bmi<18.5:
#     print('niedowaga')
# elif bmi<25:
#     print('masa ok')
# elif bmi<30:
#     print('lekka niedowzrosłość')
# elif bmi<35:
#     print('I stopień przypakowania')
# elif bmi<40:
#     print('II stopień przypakowania')
# else:
#     print('Magda Gessler')

# if bmi<16:
#     print('wyglodzenie')
# elif bmi>=16 and bmi<=16.99:
#     print('wychudzenie')

# if bmi>18.5 and bmi<25:
#     pass

# sl=dict()
# sl[1]='jeden'
# sl[2]='dwa'
# sl[3]='trzy'
#
# print(sl[2])
#
# x=1
# print('jeden' if x==1 else 'inny')
# if x==1:
#     print('jeden')
#
# while True:
#     pass

# for x in range(10):
#     print('hello')

# for x in range(10):
#     print(f'hello {x}')

#
# for x in range(1,11):
#     print(f'hello {x}')

#
# for x in range(1,11,2):
#     print(f'hello {x}')
#
# suma=0
# for x in range(1,11):
#     suma=suma+x
# print(suma)


# suma=0
# for x in range(1,11):
#     #suma=suma+x
#     suma+=x
# print(suma)

# 5. Wyświetl 20 kolejnych potęg liczby 2
#
# x=0
# for e in range(1,21):
#     x=e*0.5
#     print(x)
#
#
# for p in range(1,21):
#     print(p,pow(2,p))

# for x in range(-10,11):
#     if x<0:
#         print(f'ujemna {x}')
#     elif x==0:
#         print(f'zero {x}')
#     else:
#         print(f'dodatnia {x}')


# 6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
#  parzysta czy nieparzysta
#
# print(11%2)
# if 11%2==0:
#     print('parzysta')
# else:
#     print('nieparzysta')

#
# for x in range(1,101):
#     if x%2==0:
#         print(f'{x} jest parzyste')
#     else:
#         print(f'{x} jest nieparzyste')

# 7. Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakladamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
# oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
# Kapitalizacja comiesięczna


# konto=100000
# oprocentowanie=0.08
# ilosc_miesiecy=24
# for m in range(1,ilosc_miesiecy+1):
#     konto=round(konto+(konto*oprocentowanie/12),2)
#     print(m,konto)
#
# konto=100000
# poczatkowo=konto
# oprocentowanie=0.08
# ilosc_miesiecy=24
# for m in range(1,ilosc_miesiecy+1):
#     konto=round(konto+(konto*oprocentowanie/12),2)
#     print(m,konto)
# print(f'zarobiłeś {round(konto-poczatkowo,2)}')


# konto=100000
# poczatkowo=konto
# oprocentowanie=-0.19
# ilosc_miesiecy=24
# for m in range(1,ilosc_miesiecy+1):
#     konto=round(konto+(konto*oprocentowanie/12),2)
#     print(m,konto)
# print(f'zarobiłeś {round(konto-poczatkowo,2)}')
#
#
# while True:
#     print('prawda')
#
# while 1==1:
#     print('1==1')
#
# suma=0
# x=0
# while suma<=100:
#    x+=1
#    suma+=x
#    print(suma)


#
# suma=0
# x=0
# while suma<=100:
#    print(suma)
#    x+=1
#    suma+=x

# 8. Napisz korzystajac z petli while program który wyświetli
# 10 kolejnych potęg liczby 2.

#
# x=0
# while x<10:
#     x+=1
#     print(x,pow(2,x))
#

# przerwa do 11:39

# 9. Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość
# potęgi nie przekroczy wartości podanej przez użytkownika
#
# max=float(input('podaj max:\n'))
# wynik=0
# x=0
# while wynik<=max:
#    x+=1
#    wynik=pow(2,x)
#    print(wynik)
#
#
# max=float(input('podaj max:\n'))
# wynik=0
# x=0
# while wynik<=max:
#    print(wynik)
#    x+=1
#    wynik=pow(2,x)

# import random
# print(random.random())
# print(random.randint(1,100))

# 10. Napisz program który będzie dodawał kolejne losowe wartości z zakresu
# od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej od
# wartosci podanej przez uzytkownika

# import random
# max=float(input('podaj max wartość:\n'))
# suma=0
# while suma<max:
#     suma+=random.randint(1,10)
#     print(suma)
#
# lista=[1,2,3,4,5,'nietoperz']
#
# for e in lista:
#     print(e)

# tekst='siała BABA mak i dostała 10 lat bo nie płaciła VAT'
# # print(tekst)
# # print(tekst.upper())
# # print(tekst.lower())
# # print(tekst.title())
# # print(tekst.replace('a','X'))
# # print(tekst.lower().replace('a','X'))
# # print(len(tekst))
# # lista=[1,2,3,4,5]
# # print(len(lista))
# # szukane=input('podaj czego szukasz:\n')
# # if szukane.lower() in tekst.lower():
# #     print('jest')
# # else:
# #     print('nie ma')
# print(tekst.count('a'))
# print(tekst.lower().count('a'))

# 11. Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie z
# niego znaki ,.!? i wyświetli powiększony do dużych liter na konsoli
#
# tekst='siala baba mak'
# tekst=tekst.upper()
# print(tekst)

# odebrane=input('podaj tekst:\n')
# print(odebrane.replace(',','').replace('.','').replace('!','').replace('?','').upper())

# odebrane=input('podaj tekst:\n')
# niechciane=['!','?','.',',']
# for n in niechciane:
#     odebrane=odebrane.replace(n,'')
# print(odebrane.upper())
#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(linia)

#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(linia.replace('a','X'))

#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(len(linia.strip()),linia.strip())

# 12. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik
#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     if len(linia.strip())>0:
#         print(linia.strip())
#
# nazwa_pliku=input('nazwa pliku:\n')
# for linia in open(nazwa_pliku,encoding='utf-8'):
#     if len(linia.strip())>0:
#         print(linia.strip())

# calosc=open('tadzio.txt',encoding='utf-8').read()
# print(calosc.replace('a','X'))
# print('cośtam')
# 13. Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu tekstowego
# podanego przez użytkownika w pliku którego nazwę również poda użytkownik.

# nazwa_pliku=input('podaj nazwę pliku:\n')
# szukane=input('podaj szukaną frazę:\n')
# ilosc_wystapien=open(nazwa_pliku,encoding='utf-8').read().upper().count(szukane.upper())
# print(f'ilosc_wystapien={ilosc_wystapien}')
#

# 14. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
# poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#  linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka po
#    odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
#  i  w jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.
#
# szukane=input('podaj szukaną frazę:\n')
# plik=input('podaj nazwę pliku:\n')
# x=0
# for linia in open(plik,encoding='utf-8'):
#     x+=1
#     if szukane.lower() in linia.lower():
#         print(x,linia.strip())
#
#

# pandas

# tekst='siała baba mak nie wiedziala jak'
# print(tekst)
# print(tekst[0:10])
# print(tekst[3:10:2])


# 15. Napisz program który będzie od uzytkownika przyjmowal nazwę pliku z kodem pythona.
# Program ma wyświetlić wszystkie linie które nie są w całości komentarzami wraz z numerami tych linii w pliku

# print('dupa') #komentarz
# komentarz
# komentarz

# znak!='#'
# znak<>'#'

# plik=input('podaj nazwę pliku:\n')
# x=0
# for linia in open(plik,encoding='utf-8'):
#     x+=1
#     if len(linia.strip())>0 and linia.strip()[0:1]!='#':
#         print(x,linia.strip())

# PRZERWA OBIADOWA DO 13:25
#
# lista=[1,'dżem pomarańczowy','koza',4]
# #lista=[]
# lista.append('dodany element')
# print(lista)
# print(lista[0])
# print('######')
# for element in lista:
#     print(element)

# 16. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.
#
# potegi=[]
# for x in range(1,11):
#     potegi.append(pow(2,x))
# print(potegi)
# for p in potegi:
#     print(p)

# lista1=[1,2,3,4]
# lista2=lista1
# lista1.clear()
# print(lista1)
# print(lista2)
#
# lista1=[1,2,3,4]
# lista2=lista1.copy()
# lista1.clear()
# print(lista1)
# print(lista2)
#
# lista=[1,2,3]
# druga_lista=['lubie','pierogi']
# lista.append(druga_lista)
# print(lista)


# lista=[1,2,3]
# druga_lista=['lubie','pierogi']
# lista.extend(druga_lista)
# print(lista)
#
# lista=[1,2,3]
# druga_lista=['lubie','pierogi']
# suma=lista+druga_lista
# print(suma)

#
# lista=[1,2,3]
# druga_lista=['lubie','pierogi']
# suma=[*lista,*druga_lista]
# print(suma)
#
# lista=[1,2,3]
# print(lista)
# print(*lista)

#
# lista=[1,2,3]
# druga_lista=['lubie','pierogi']
# suma=[*lista,*druga_lista]
# suma=[1,2,3,'lubie','pierogi']
# print(suma)
#
# def funkcja(*args):
#     pass
#
# lista=[1,2,3]
# druga_lista=['lubie','pierogi']
# suma=[]
# suma.append(lista)
# suma.append(druga_lista)
# print(suma)

# 17.Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)


# import random
#
# lista1 = []
# lista2 = []
# for x in range(10):
#     lista1.append(random.randint(1, 10))
#     lista2.append(random.randint(1, 10))
# print(lista1)
# print(lista2)
# suma=[*lista1,*lista2]
# print(suma)
# lista1.extend(lista2)
# print(lista1)
#
# lista=[]
# lista.append([2,4])
# lista.append([3,8])
# print(lista)
# print(lista[1])
# print(lista[1][1])

# 18. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
#
# lista=[]
# for x in range(1,11):
#     lista.append([x,pow(2,x)])
# print(lista)

# lista=[]
# for x in range(1,11):
#     lista.append(x)
# print(lista)
#
# lista=[x for x in range(1,11)]
# print(lista)
#
# lista=[]
# for x in range(1,11):
#     lista.append(x*1000)
# print(lista)
#
# lista=[x*1000 for x in range(1,11)]
# print(lista)

# lista=[1,2,3,4,5,6,7,8]
# wynik=[e*100 for e in lista]
# print(wynik)

# import random
# wynik=[random.randint(1,10) for e in range(10)]
# print(wynik)
#
# lista=[]
# for x in range(1,11):
#     if x%2==0:
#         lista.append(x)
# print(lista)
#
# lista=[x for x in range(1,11) if x%2==0]
# print(lista)
# print([x for x in range(1,11) if x%2==0])


# send_mail('tytul','tresc',[e.email for e in get_all_participants(1)])


# 19. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2

# lista=[]
# for x in range(1,11):
#     lista.append(pow(2,x))
# print(lista)
#
# lista=[pow(2,x) for x in range(1,11)]
# print(lista)
# print([pow(2,x) for x in range(1,11)])
#

# 20. Korzystając z list składanych wygeneruj listę 10 elementow której każdy element również będzie listą.
# Pierwszy element tej podlisty to numer potegi, a drugi to wartosc tej potegi dla liczby 2
#
# [
#     [1,2],
#     [2,4],
#     [3,8]
# ]

# lista = []
# for x in range(1, 11):
#     lista.append([x, pow(2, x)])
# print(lista)
#
# lista = [[x, pow(2, x)] for x in range(1, 11)]
# print(lista)
# print([[x, pow(2, x)] for x in range(1, 11)])
#
#
# linia='1;Andrzej;Klusiewicz;1.76;80'
# print(linia.split(';'))
# print(linia.split(';')[2].upper())
# lista=linia.split(';')
# print(lista[2].upper())

# 21. Napisz program który z pliku dane.csv wyświetli powiekszone imiona i nazwiska oraz wzrost i masę
#
# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     #print(lista)
#     #lista = linia.split(';')
#     print(lista[1].upper(),lista[2].upper(),lista[3],lista[4])

# 22. Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.csv
# w taki sposób   by linie oczyścic z bialych znaków i rozbić na listy.
# Każdy z elementów listy sam   powinien byc listą. Następnie przeiteruj po wyniku
# i wyświetl wszystkie elementy listy  linia po linii.
#
# lista=[]
# for e in lista:
#     print(e)
#
# lista=[]
# for linia in open('dane.csv',encoding='utf-8'):
#     podlista=linia.strip().split(';')
#     lista.append(podlista)
#
# for e in lista:
#     print(e)

# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     print(l)
#
# for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     print(l)

#
# for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]:
#     print(l)
#

# 23. Dla każdego wpisu w pliku dane.csv wyświetl na konsoli dane o
# id, imieniu, nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika

# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for e in lista:
#     wzrost=float(e[3])
#     masa=float(e[4])
#     bmi=round(masa/pow(wzrost,2),2)
#     print(*e,bmi)

# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for e in lista:
#     wzrost=float(e[3])
#     masa=float(e[4])
#     bmi=round(masa/pow(wzrost,2),2)
#     e.append(bmi)
#     print(*e)

# for e in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     e.append(round(float(e[4])/pow(float(e[3]),2),2))
#     print(*e)
#
# for e in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     e.append(round(float(e[4])/pow(float(e[3]),2),2))
#     print(*e)
#
# suma=0
# for i in range(1,11):
#     suma+=i

# przerwa do 15:09

# lista=[3,2,1,7,6,4,2,1]
# druga=sorted(lista)
# print(druga)
#
# lista=[3,2,1,7,6,4,2,1]
# lista.sort()
# print(lista)
#
# lista=[3,2,1,7,6,4,2,1]
# druga=sorted(lista)
# druga=list(reversed(druga))
# print(druga)


#
# lista=[3,2,1,7,6,4,2,1]
# druga=sorted(lista, reverse=True)
# print(druga)

# #
# lista=[3,2,1,7,6,4,2,1]
# lista.sort(reverse=True)
# print(lista)


# lista=[3,2,1,7,6,4,2,1]
# lista.sort()
# lista.reverse()
# print(lista)

# lista=[1,4,3,2,'koza']
# lista.sort()
#
# lista=['1','4','3','2','11','22','koza']
# lista.sort()
# print(lista)
#
# lista=[1,6,34,2,3]
# print(lista.sort())
# print(sorted(lista))

# 24. Wygeneruj listę 10 elementów o losowej wartości liczbowej, posortuj listę
# i wyświetl jej zawartość linia po linii
#
# import random
# print(round(random.random()*100000))
#
# import random
# lista=[random.randint(1,10) for _ in range(10)]
# print(lista)
# lista.sort()
# print(lista)
# for e in lista:
#     print(e)


# import random
# lista=[random.randint(1,10) for _ in range(10)]
# print(lista)
# for e in sorted(lista):
#     print(e)
#
# import random
# lista=sorted([random.randint(1,10) for e in range(10)])
# print(lista)
# for e in lista:
#     print(e)

# for _ in range(1,11):
#     print('dupa')

# lista = [
#     [1, 'B'],
#     [3, 'A'],
#     [2, 'C']
# ]
#
# lista.sort()
# print(lista)
#
# import operator
# lista = [
#     [1, 'B'],
#     [3, 'A'],
#     [2, 'C']
# ]
# lista.sort(key=operator.itemgetter(1))
# print(lista)


# import operator
# lista = [
#     [1, 'B'],
#     [3, 'A'],
#     [2, 'C']
# ]
# lista.sort(key=operator.itemgetter(1),reverse=True)
# print(lista)
#
# lista = [
#     [1, 'B'],
#     [3, 'A'],
#     [2, 'C']
# ]
# lista.sort(key=lambda x:x[1])
# print(lista)
#
# class Osoba:
#     first_name=None
#     last_name=None
#     def __init__(self,f,l):
#         self.first_name=f
#         self.last_name=l
#     def __str__(self):
#         return str(self.__dict__)
#
# lista=[Osoba('Andrzej','Klusiewicz'),Osoba('Monika','Bożko'),Osoba('Natalia','Gmurczyk')]
# lista.sort(key=lambda o:o.last_name)
# for l in lista:
#     print(l)

# def powieksz(t):
#     return t.upper()
#
# def funkcja(f,t):
#     print(f(t))
#
# funkcja(powieksz,'oko')
#
# def funkcja(f,t):
#     print(f(t))
#
# funkcja(lambda e:e.upper(),'oko')


# import operator
# lista = [
#     [1, 'B'],
#     [3, 'A'],
#     [2, 'C']
# ]
# lista.sort(key=operator.itemgetter(1))
# lista.sort(key=lambda x:x[1])
# print(lista)

# 25.Wczytaj do listy kolejne wiersze z pliku dane.csv.
# Dane posortuj po nazwiskach i wyswietl linia po linii na konsoli.


# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# print(lista)
# lista.sort(key=lambda x:x[2])
# print(lista)

# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# wynik=sorted(lista,key=lambda x:x[2])
# print(wynik)

# from operator import itemgetter
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# lista.sort(key=itemgetter(2))
# print(lista)
#
# from operator import itemgetter
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# lista=sorted(lista,key=itemgetter(2))
# print(lista)


#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for w in sorted(lista,key=lambda x:x[2]):
#     print(w)

# 26.Wyświetl na konsoli linia po linii dane z pliku dane.csv ale posortowane  malejąco wg. bmi

# lista=[e.strip().split(';') for e in open('dane.csv', encoding='utf-8')]
# for e in lista:
#     wzrost=float(e[3])
#     masa=float(e[4])
#     bmi=round(masa/pow(wzrost,2),2)
#     e.append(bmi)
#
# lista.sort(key=lambda x:x[5],reverse=True)
#
# for e in lista:
#     print(e)
#
#
# from operator import itemgetter
# lista=[e.strip().split(';') for e in open('dane.csv', encoding='utf-8')]
# for e in lista:
#     wzrost=float(e[3])
#     masa=float(e[4])
#     bmi=round(masa/pow(wzrost,2),2)
#     e.append(bmi)
#
# lista.sort(key=itemgetter(5),reverse=True)
#
# for e in lista:
#     print(e)
# #
# import os
# for e in os.walk('e:\\'):
#     print(e)
# import os
# sciecha=os.path.join('e:\\','PostgreSQL')
# print(sciecha)


# tekst="siała baba mak"
# if "baba" in tekst:
#     print('jest')
# else:
#     print('nie ma')

# lista=['siała','baba','mak']
# if 'ba' in lista:
#     print('jest')
# else:
#     print('nie ma')

#
#
# lista=['siała','baba','mak']
# for e in lista:
#     if 'ba' in e:
#         print(f'jest w {e}')
#     else:
#         print(f'nie ma w {e}')

# 27. Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
# Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi zawierajace w nazwie szukaną
# frazę - wraz ze ścieżkami. Wyszukiwarka ma być nieczuła na wielkość liter
#
# import os
# startowa="e:\\"
# szukane="oracle"
# for e in os.walk(startowa):
#     for k in e[1]:
#         if szukane.upper() in k.upper():
#             print(os.path.join(e[0],k))
#     for p in e[2]:
#         if szukane.upper() in p.upper():
#             print(os.path.join(e[0],p))

#
# lista=['a','b','c']
# lista2=[e.upper() for e in lista]
# print(lista2)

# krotka.sort()
# krotka=()
# print(krotka)

# krotka=(1,2,3,4,5)
# print(krotka)
# krotka[3]='cos innego'
#
# krotka=[1,2,3,4,5]
# krotka[3]='cos innego'
# print(krotka)

# krotka=(4,7,1,2)
# print(sorted(krotka))
#
# krotka=(4,7,1,2)
# lista=list(krotka)
# lista.sort()
# krotka=tuple(lista)
# print(krotka)
# print(lista)
# krotka=(4,7,1,2)
# print(krotka[2])
# for e in krotka:
#     print(e)

# 28. Stwórz dwie krotki.
# Jedna ma zawierać 10 losowych liczb zakresu 1-10, druga 10 losowych liczb zakresu 11-20.
# Stwórz trzecią krotkę która ma zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli

# lista=[1,2,3]
# print(lista)
# print(*lista)
# krotka=(1,2,3)
# print(krotka)
# print(*krotka)
# wynik=(*lista,*krotka)
# print(wynik)
# import random
# krotka1=tuple([random.randint(1,10) for e in range(10)])
# krotka2=tuple([random.randint(11,20) for e in range(10)])
# suma=(*krotka1,*krotka2)
# print(krotka1)
# print(krotka2)
# print(suma)


# 29. Napisz kod ktora wyświetli w postaci listy krotek zawartość pliku dane.csv
#
# wynik=[ tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]
# for w in wynik:
#     print(w)

# przerwa do 10:18

# zestaw={1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3}
# zestaw.add(4)
# print(zestaw)
# for z in zestaw:
#     print(z)


# lista=[1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
# print(lista)
# zestaw=set(lista)
# lista=list(zestaw)
# print(lista)
#
#
# z1={1,2,3,4,5,6}
# z2={4,5,6,7,8,9}
#
# print('część wspólna=', z1.intersection(z2))
# print('z1-z2=', z1.difference(z2))
# print('z2-z1=', z2.difference(z1))
# print('suma=',z1.union(z2))
#

# 30. Wygeneruj dwa zestawy, dodaj do nich po 20
# (w przypadku duplikatów lista może być mniejsza niż 20 elementów)
# losowych liczb z zakresu 1-40. Wyswietl ich sumę, różnicę i część wspólną

# import random
# z1 = set()
# z2 = set()
# for x in range(20):
#     z1.add(random.randint(1, 40))
#     z2.add(random.randint(1, 40))
# print(z1)
# print(z2)
# print('część wspólna=', z1.intersection(z2))
# print('z1-z2=', z1.difference(z2))
# print('z2-z1=', z2.difference(z1))
# print('suma=',z1.union(z2))


# import random
# z1=set([random.randint(1,40) for e in range(20)])
# z2=set([random.randint(1,40) for e in range(20)])
# print(z1)
# print(z2)
# print('część wspólna=', z1.intersection(z2))
# print('z1-z2=', z1.difference(z2))
# print('z2-z1=', z2.difference(z1))
# print('suma=',z1.union(z2))

#
# lista=[
#     (1,'A'),
#     (2,'C'),
#     (1,'A')
# ]
#
# print(lista)
# zestaw=set(lista)
# print(lista)

#31. Zduplikuj jeden z wierszy w pliku dane.csv. Napisz kod który zwróci do postaci
# listy krotek zawartość tego pliku z danymi bez powtórek.
#
# wynik=[tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]
# bez_duplikatow=list(set(wynik))
# for bd in bez_duplikatow:
#     print(bd)

# for bd in list(set([tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')])):
#     print(bd)

#32. Przetwórz plik dane.csv w taki sposób by w efekcie umieścić w pliku output.csv
# dane z pliku dane.csv wzbogacone o obliczone BMI, bez duplikatów i rozwiązując problem
# podania przecinka w miejsce kropki we wzroście i masie oraz problem z pustymi wierszami.

#
# plik=open('pliczek.txt',encoding='utf-8',mode='w')
# for x in range(1,11):
#     plik.write(f"linia {x}\n")
# plik.close()
#
# lista=['1','Andrzej','Klusiewicz','1.76','80']
# linia_csv=";".join(lista)
# print(linia_csv)


# lista=['1','Andrzej','Klusiewicz','1.76','80',str(25)]
# linia_csv=";".join(lista)
# print(linia_csv)

# dane=[e.strip().replace(',','.').split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]
# for d in dane:
#     d.append(str(round(float(d[4])/pow(float(d[3]),2),2)))
# bez_duplikatow=list(set([tuple(d) for d in dane]))
# plik=open('output.csv',encoding='utf-8',mode='w')
# for bd in bez_duplikatow:
#     plik.write(";".join(bd)+'\n')
# plik.close()


# dane=[e.strip().replace(',','.').split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]
# for d in dane:
#     d.append(str(round(float(d[4])/pow(float(d[3]),2),2)))
# bez_duplikatow=list(set([tuple(d) for d in dane]))
# with open('output.csv',encoding='utf-8',mode='w') as plik:
#     for bd in bez_duplikatow:
#         plik.write(";".join(bd)+'\n')


# dane=[e.strip().replace(',','.').split(';') for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]
# for d in dane:
#     d.append(str(round(float(d[4])/pow(float(d[3]),2),2)))
# with open('output.csv',encoding='utf-8',mode='w') as plik:
#     for bd in list(set([tuple(d) for d in dane])):
#         plik.write(";".join(bd)+'\n')

#przerwa do 11:30
#
# slownik=dict()
# slownik['moj_klucz']=1234
# slownik['inny_klucz']="siała baba mak"
# slownik['lista']=[1,2,3,4,5]
#
# #print(slownik['inny_klucz'])
# #print(slownik['dupa'])
# for k in slownik.keys():
#     print(k,slownik[k])

#
# slownik=dict()
# slownik['moj_klucz']=1234
# slownik['inny_klucz']="siała baba mak"
# slownik['lista']=[1,2,3,4,5]
#
# del slownik['lista']
# #print(slownik['inny_klucz'])
# #print(slownik['dupa'])
# for k in slownik:
#     print(k,slownik[k])
#
# for v in slownik.values():
#     print(v)

#33. Stwórz plik ustawienia.conf i umieść w nim poniższe dane
# encoding;utf-8
# timezone;-2
# color;black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila
# klucze a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości

# lista=[e.strip().split('=') for e in open('ustawienia.conf',encoding='utf-8')]
# ustawienia=dict()
# for l in lista:
#     ustawienia[l[0]]=l[1]
#
# for k in ustawienia:
#     print(k,ustawienia[k])

#34. Wczytaj do słownika dane z pliku dane.csv tak by kluczem było imię sklejone
# z nazwiskiem rozdzielone spacja, a pozostałe dane znalazły się w wartości
# jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość.

#
# sl=dict()
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     klucz=l[1]+" "+l[2]
#     wartosc=[l[0],l[3],l[4]]
#     sl[klucz]=wartosc
#
# for k in sl:
#     print(k,sl[k])

#35. Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
#    Wynik powinien byc posortowany malejąco wg ilosci wystapien
#    a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej listy.
#       Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc.
#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
#    c) Przepakuj dane ze słownika do listy i posortuj.
#
# [
#     ("tadeusz",100),
#     ('dupa',50),
#     ('koń',30)
# ]
#
# Tadeusz
# Tadeusz,
# Tadeusz!
# Tadeusz?

# sl=dict()
# sl['klucz']=11111

# if 'klucz' in sl:
#     print('mamy taki klucz')
# else:
#     print('nie mamy takiego klucza')
#
# import time
# poczatek=time.time()
# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# niechciane=['!','?',',','.','...','/','-','_',':','(',')',';','…']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slowa=calosc.split()
# for s in slowa:
#     print(s,slowa.count(s))
# koniec=time.time()
# print(f'czas trwania {koniec-poczatek}s')

#
#
# import time
# poczatek=time.time()
# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# niechciane=['!','?',',','.','...','/','-','_',':','(',')',';','…']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slowa=calosc.split()
# sl=dict()
# for s in slowa:
#     if s in sl:
#         sl[s]+=1
#     else:
#         sl[s]=1
# wynik=[]
# for k in sl:
#     wynik.append( [k,sl[k]] )
# wynik.sort(key=lambda e:e[1], reverse=True)
# for w in wynik:
#     print(w)
# koniec=time.time()
# print(f'czas trwania {koniec-poczatek}s')


#PRZERWA OBIADOWA DO 13:15

#36. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.
#
# for x in range(-10,11):
#     print(1/x)

# try:
#     print(1/0)
# except:
#     print('jakiś error')
# print('cośtam dalej')
#
# try:
#     print(1/0)
# except Exception as e:
#     print(f'error={e}')
# print('cośtam dalej')

#
#
# try:
#     print(1/0)
# # except ZeroDivisionError:
# #    print(f'nie dziel przez zero')
# except IndexError:
#     print(f'to się nie ma prawa zdarzyć')
# except KeyError:
#     print(f'to też się nie ma prawa zdarzyć')
# except Exception as e:
#     print(f'inny wyjątek e={e} type(e)={type(e)}')
#
# print('cośtam dalej')


# #raise ZeroDivisionError
# raise Exception('kij ci w oko')

#37. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10 w taki
#sposob by w przypadku wyjatku nie przerywac dzialania petli a po prostu wyswietlic na konsoli
# informację o błędzie i przejsc do dalszego przetwarzania

#
# try:
#     for x in range(-10,11):
#         print(x,1/x)
# except ZeroDivisionError:
#     print('DZIELENIE PRZEZ ZERO')
#
# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except ZeroDivisionError:
#         print(f'dzielenie przez zero na x={x}')

#38. Przetwórz wszystkie wiersze z dane.csv wyswietlajac na konsoli dane z
# wiersza wzbogacone o bmi. Nie podmieniaj przecinków etc w tekscie. W przypadku pojawienia się
# wyjątku na obliczaniu bmi dla   któregoś wiersza chcemy go zapisać (cały wiersz) w osobnym pliku bledy.csv
# wzbogacony o informację o rodzaju błędu
#4;Andrzej;1,89;90;IOERROR
#
#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for e in lista:
#     try:
#         bmi=round(float(e[4])/pow(float(e[3]),2),2)
#         print(e,bmi)
#     except Exception as ex:
#         with open('errors.csv',encoding='utf-8',mode='a') as plik:
#             plik.write(';'.join(e)+f";{ex}\n")


# def witacz():
#     print('siema!')
#
# witacz()
#
# def witacz():
#     print('siema!')
# def witacz(imie,nazwisko):
#     print(f'siema {imie} {nazwisko}!')
#
# witacz()

#
# def pomnoz(x,y):
#     return x*y



# def pomnoz(x,y):
#     z=x*y
#     return z
#     print('dupa') #nigdy nie zostanie wykonane
#
# print(pomnoz(10,6))
# wynik=pomnoz(111,333)
# print(wynik)


#39. Stwórz funkcję która przyjmie wzrost i masę a zwróci zaokraglone do 2 miejsc po przecinku BMI.
# W przypadku pojawienia się wyjątku, wyświetl na konsoli jaki wystąpił problem a z funkcji zwróć -1.

#
# def bmi(w,m):
#     try:
#         return round(m/pow(w,2),2)
#     except ZeroDivisionError:
#         print('podałeś zerowy wzrost')
#         return -1
#     except Exception as e:
#         print(f'jakiś inny wyjątek={e}')
#         return -1
#
# #bmi(0,80)
# bmi('dupa','dupa')

# def witacz(imie,nazwisko):
#     print(f'witaj {imie} {nazwisko}!')
#
# witacz('Andrzej','Klusiewicz')

# def witacz(imie='nie podano',nazwisko='nie podano'):
#     print(f'witaj {imie} {nazwisko}!')
#
# witacz()


# def witacz(imie,nazwisko='nie podano'):
#     print(f'witaj {imie} {nazwisko}!')
#
# witacz('Andrzej')


# def witacz(imie='Andrzej',nazwisko): #fuuuuuu
#     print(f'witaj {imie} {nazwisko}!')
#
# witacz('Andrzej')


#40. Napisz funkcję która zwróci pod postacią listy krotek zawartość pliku
  # którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty z kodowaniem
  # podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie pdane ma przyjac utf-8

# def parse_csv(file_name,enc='utf-8'):
#     return [e.strip().split(';') for e in open(file_name,encoding=enc)]
#
# for e in parse_csv('dane.csv'):
#     print(e)

# for e in parse_csv('dane.csv','utf-8'):
#     print(e)

# def parse_csv(file_name,enc='utf-8',divisor=';'):
#     return [e.strip().split(divisor) for e in open(file_name,encoding=enc)]
#
# for e in parse_csv('dane.csv','utf-8',';'):
#     print(e)

#41.Napisz funkcję która bedzie w stanie przyjąć taką listę jaka jest zwracana
 # przez funkcję z poprzedniego ćwiczenia. Funkcja ta ma przeiterować po otrzymanej
 # liście i wyświetlić każdy element na konsoli. Odbierz dane z funkcji z ćwiczenia
 # poprzedniego i przekaz do nowo powstalej funkcji.

#
# def parse_csv(file_name,enc='utf-8',divisor=';'):
#     return [e.strip().split(divisor) for e in open(file_name,encoding=enc)]
#
# def print_csv(data):
#     for d in data:
#         print(d)
#
# dane=parse_csv('dane.csv')
# print_csv(dane)
#
# print_csv(parse_csv('dane.csv'))

#42. Napisz funkcję która przyjmie przez argumenty kwotę lokaty, oprocentowanie w skali roku, ilosc miesięcy.
# Funkcja ma zwrócić zarobek na lokacie o podanych parametrach

# def lokata(konto,oprocentowanie,ilosc_miesiecy):
#     poczatkowo=konto
#     for m in range(1,ilosc_miesiecy+1):
#         konto=round(konto+(konto*oprocentowanie/12),2)
#         #print(m,konto)
#     return round(konto-poczatkowo,2)
#
# print( lokata(100000,0.08,24) )


#przerwa do 14:30

# import matematyka
# print(matematyka.dodawanie(10,30))


# import matematyka as m
# print(m.dodawanie(10,30))

#from operator import itemgetter
#
# from matematyka import dodawanie
# print(dodawanie(1,2))

# from matematyka import dodawanie,odejmowanie
# print(dodawanie(1,2))

# from matematyka import *
# print(dodawanie(1,2))

# from invoice_dao import *
# from todos_dao import *
# print(get_all())

# import invoice_dao as idao
# import todos_dao as tdao
# print(idao.get_all())
# print(tdao.get_all())

#import matematyka

#import this

# import dao.invoice_dao
#import dao.invoice_dao as idao
#from dao.invoice_dao import *

#43.Stwórz pakiet zawierający moduł który bedzie zawierał funkcję przyjmującą wzrost i masę a zwracającą bmi.
# Zaimportuj i wywołaj tę funkcję w taki sposób by przy jej wywołaniu nie trzeba było  podawać nazwy pakietu ani modułu.
#
# from cwiczenie43.modul import *
# print(bmi(1.76,80))

# import requests
# response=requests.get('https://jsystems.pl/static/blog/python/dane.json')
# print(response.status_code)
# if response.status_code==200:
#     dane=response.json()
#     print(dane)
#     print(dane['nazwisko'])
#     adres=dane['adres']
#     print(adres['miasto'])
#     print(dane['adres']['miasto'])
#     for j in dane['jezyki']:
#         print(j)
#
# def funkcja():
#     pass
#
# import requests
# dane=dict()
# response=requests.post('https://jsystems.pl/static/blog/python/dane.json',data=dane,headers={"Content-Type":"application/json"})
# print(response.status_code)

#44. z usługi sieciowej http://jsystems.pl/Universe/samaTabelka.do pobierz informację o szkoleniach.
# na konsoli wyswietl tytuly, miasta i daty wszystkich szkolen które w tytule mają malymi badz duzymi
# literami "Java" lub "JavaScript" i status terminu gwarantowanego (pole terminyGwarantowany=1)
