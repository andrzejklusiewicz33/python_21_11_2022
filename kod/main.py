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

weight=float(input('podaj masę:\n'))
height=float(input('podaj wzrost:\n'))
bmi=round(weight/pow(height,2),2)
print(bmi)
