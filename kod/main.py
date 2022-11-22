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

#25.Wczytaj do listy kolejne wiersze z pliku dane.csv.
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

#26.Wyświetl na konsoli linia po linii dane z pliku dane.csv ale posortowane  malejąco wg. bmi

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

#27. Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
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

#krotka.sort()
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

#28. Stwórz dwie krotki.
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


#29. Napisz kod ktora wyświetli w postaci listy krotek zawartość pliku dane.csv
