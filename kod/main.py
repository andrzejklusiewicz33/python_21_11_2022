#dodatki:
#dekoratory
#obiektowość
#Faker
# print("hello")
# print('hello')
# print("Mc'Donalds")
# x='koza'
# print(x,type(x))
# x=10
# print(x,type(x))
# x=1.3
# print(x,type(x))
#x='nietoperz'
#print('x='+x)
#x=10
#print('x='+x)
#print('x='+str(x))
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

#print('hajs '*100)

#x=int(input('podaj x:\n'))
# x=float(  input('podaj x:\n')    )
# print(type(x))
# print(x/3)

#1. Napisz program który przyjmie od uzyszkodnika jego imie oraz nazwisko, a nastepnie
#wyswietli komunikat typu "Witaj Andrzej Klusiewicz!"
#PEP8
#import this
# first_name=input('podaj imię:\n')
# last_name=input('podaj nazwisko:\n')
# print("Witaj "+first_name+" "+last_name+"!")
# print("Witaj {} {}!".format(first_name,last_name))
# print(f'Witaj {first_name} {last_name}!')
#

#2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika jego masę
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

#przerwa do 10:23

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


#3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić
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


#4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
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

#5. Wyświetl 20 kolejnych potęg liczby 2
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


#6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
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

#7. Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
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

#8. Napisz korzystajac z petli while program który wyświetli
# 10 kolejnych potęg liczby 2.

#
# x=0
# while x<10:
#     x+=1
#     print(x,pow(2,x))
#

#przerwa do 11:39

#9. Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość
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

#10. Napisz program który będzie dodawał kolejne losowe wartości z zakresu
#od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej od
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

#11. Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie z
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

#12. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik
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
#print('cośtam')
#13. Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu tekstowego
# podanego przez użytkownika w pliku którego nazwę również poda użytkownik.

# nazwa_pliku=input('podaj nazwę pliku:\n')
# szukane=input('podaj szukaną frazę:\n')
# ilosc_wystapien=open(nazwa_pliku,encoding='utf-8').read().upper().count(szukane.upper())
# print(f'ilosc_wystapien={ilosc_wystapien}')
#

#14. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
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

#pandas

# tekst='siała baba mak nie wiedziala jak'
# print(tekst)
# print(tekst[0:10])
# print(tekst[3:10:2])


#15. Napisz program który będzie od uzytkownika przyjmowal nazwę pliku z kodem pythona.
# Program ma wyświetlić wszystkie linie które nie są w całości komentarzami wraz z numerami tych linii w pliku

#print('dupa') #komentarz
#komentarz
    #komentarz

# znak!='#'
# znak<>'#'

# plik=input('podaj nazwę pliku:\n')
# x=0
# for linia in open(plik,encoding='utf-8'):
#     x+=1
#     if len(linia.strip())>0 and linia.strip()[0:1]!='#':
#         print(x,linia.strip())

#PRZERWA OBIADOWA DO 13:25
#
# lista=[1,'dżem pomarańczowy','koza',4]
# #lista=[]
# lista.append('dodany element')
# print(lista)
# print(lista[0])
# print('######')
# for element in lista:
#     print(element)

#16. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
#Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.
