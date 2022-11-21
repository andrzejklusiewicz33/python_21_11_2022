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
