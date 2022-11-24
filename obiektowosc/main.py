# class Person:
#     first_name=None
#     last_name=None
#
# p1=Person()
# p1.first_name='Andrzej'
# p1.last_name='Klusiewicz'
#
# p2=Person()
# p2.first_name='Bartłomiej'
# p2.last_name='Juszczak'
#
# print(p1.first_name,p1.last_name)
# print(p2.first_name,p2.last_name)
#
# class Person:
#     first_name=None
#     last_name=None
#     def funkcja(self):
#         print('no siema!')
#
# p1=Person()
# p1.first_name='Andrzej'
# p1.last_name='Klusiewicz'
# p1.funkcja()
# print(p1.first_name, p1.last_name)



# class Person:
#     first_name=None
#     last_name=None
#     def show_me(self):
#         print(f'first_name={self.first_name}, last_name={self.last_name}')
#
# p1=Person()
# p1.first_name='Andrzej'
# p1.last_name='Klusiewicz'
# p1.show_me()

#68. Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
# Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
# Stwórz dwa obiekty tej klasy (uzupelnij tez dane)
# i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.
# 
# class Samochod:
#     marka=None
#     model=None
#     rejestracja=None
#     def wyswietl(self):
#         print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')
# 
# s1=Samochod()
# s1.marka='Kałdi'
# s1.model="A4"
# s1.rejestracja="WWL 12345"
# 
# s2=Samochod()
# s2.marka='Czarny'
# s2.model='Ciągnik'
# s2.rejestracja='POJ 2400'
# 
# s1.wyswietl()
# s2.wyswietl()
#
# class Person:
#     first_name=None
#     last_name=None
#
#     def set_values(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#
#     def show_me(self):
#         print(f'first_name={self.first_name}, last_name={self.last_name}')
#
# p1=Person()
# p1.set_values('Twoja','Stara')
# p1.show_me()

#69. Zadbaj o to by klasa Samochod posiadała metodę pozwalającą ustawić wartości wszystkich pól.
# Jej przykładowe wywołanie: s1.ustaw_wartosci(‘Renault’,’Kadjar’,’WE968RP’)

# class Samochod:
#     '''
#     Pamiętaj o wywołaniu funkcji ustaw_wartosci po stworzeniu obiektu
#     '''
#     marka=None
#     model=None
#     rejestracja=None
#
#     def ustaw_wartosci(self,ma,mo,re):
#         self.marka=ma
#         self.model=mo
#         self.rejestracja=re
#
#     def wyswietl(self):
#         print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')

#help(Samochod)
#
#s=Samochod()
# s.ustaw_wartosci('Renault','Kadjar','WE12345')
#s.wyswietl()
#
#
# class Person:
#     first_name=None
#     last_name=None
#
#     def __init__(self,fn,ln):
#         print('konstruktor!')
#         self.first_name=fn
#         self.last_name=ln
#
#     def set_values(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#
#     def show_me(self):
#         print(f'first_name={self.first_name}, last_name={self.last_name}')

# p=Person('Andrzej','Klusiewicz')
# p.show_me()

# p=Person(None,None)
# p.show_me()

#
# class Person:
#     first_name=None
#     last_name=None
#
#     def __init__(self,fn='nie podano',ln='nie podano'):
#         self.first_name=fn
#         self.last_name=ln
#
#     def show_me(self):
#         print(f'first_name={self.first_name}, last_name={self.last_name}')
#
# p=Person()
# p.show_me()


#70. Dodaj do klasy Samochód konstruktor wymuszający ustawienie wartości wszystkich pól przy tworzeniu obiektu.
# Stworz obiekt klasy samochod i wywolaj na nim metode wyswietl

#
# class Samochod:
#     marka=None
#     model=None
#     rejestracja=None
#
#     def __init__(self,ma,mo,re):
#         self.marka=ma
#         self.model=mo
#         self.rejestracja=re
#
#     def wyswietl(self):
#         print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')
#
# s=Samochod('A','B','C')
# s.wyswietl()

#71. Stwórz klasę Zawodnik posiadającą pola wzrost i masa.
# Pola te mają być uzupełniane przy tworzeniu obiektu. Dodaj do klasy metodę get_bmi
# która zwróci obliczone na podstawie pól BMI. Powołaj do życia obiekt tej klasy
# i wyświetl na konsoli obliczone BMI.

# class Zawodnik:
#
#     def __init__(self,w,m):
#         self.wzrost=w
#         self.masa=m
#
#     def get_bmi(self):
#         return round(self.masa/pow(self.wzrost,2),2)
#
# z=Zawodnik(1.76,80)
# print(z.get_bmi())
# z.nieistniejace_pole='dupa'
# print(z.nieistniejace_pole)


#72. Stwórz plik konfiguracyjny z zawartością:
# encoding;utf-8
# timezone;-2
# color;black
# Stwórz klasę Ustawienia która będzie posiadała słownik.
# Niech każdy obiekt klasy ustawienia podczas jego tworzenia wczytuje
# do tego słownika zawartość pliku konfiguracyjnego w taki sposób,
# by pierwsza kolumna stanowiła klucze dla słownika a druga wartości.
#Przetestuj tworzenie obiektu i wyświetl zawarty w nim słownik
#
# class Ustawienia:
#     conf=dict()
#     def __init__(self):
#         for e in [line.strip().split(';') for line  in  open('config.conf',encoding='utf-8')]:
#             self.conf[e[0]]=e[1]
#
# u=Ustawienia()
# print(u.conf)
#

#przerwa do 14:36

# class Person:
#     first_name=None
#     last_name=None
#
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#     def __str__(self):
#         return f'first_name={self.first_name}, last_name={self.last_name}'
#
# p=Person('ośnieżkowany','geodeta')
# print(p)

#73. Przesłoń metodę "__str__" w klasie "Samochod". Stworz obiekt tej klasy i wyswietl jego zawartosc na konsoli.

# class Samochod:
#     marka=None
#     model=None
#     rejestracja=None
#
#     def __init__(self,ma,mo,re):
#         self.marka=ma
#         self.model=mo
#         self.rejestracja=re
#
#     def __str__(self):
#         return f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}'
#
# s=Samochod('A','B','C')
# print(s)

#74. Załaduj dane z pliku zawodnicy.csv do postaci listy obiektów.
# Następnie przeiteruj po tej liście i wyświetl zawartość każdego z obiektów
#
# class Zawodnik:
#     def __init__(self,id,imie,nazwisko,wzrost,masa):
#         self.id_zawodnika=id
#         self.imie=imie
#         self.nazwisko=nazwisko
#         self.wzrost=wzrost
#         self.masa=masa
#     def __str__(self):
#         return f"id_zawodnika={self.id_zawodnika}, imie={self.imie}, nazwisko={self.nazwisko}, wzrost={self.wzrost}, masa={self.masa}"
#
# result=[]
# for e in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     result.append(  Zawodnik(e[0],e[1],e[2],e[3],e[4])  )
#
# print(result)
# for r in result:
#     print(r)


#
# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self,fn,ln):
#         if fn is None or len(fn)==0:
#             raise Exception('imię nie może być puste')
#         if ln is None or len(ln)==0:
#             raise Exception('nazwisko nie może być puste')
#         self.first_name=fn
#         self.last_name=ln
#     def __str__(self):
#         return f'first_name={self.first_name}, last_name={self.last_name}'
#
# p=Person('Andrzej','Klusiewicz')
# p.first_name=None
# p.last_name=None
# print(p)
#
#
# class Person:
#     __first_name=None
#     __last_name=None
#
#     def set_first_name(self,fn):
#         if fn is None or len(fn)==0:
#             raise Exception('imię nie może być puste')
#         self.__first_name=fn
#
#     def set_last_name(self,ln):
#         if ln is None or len(ln)==0:
#             raise Exception('nazwisko nie może być puste')
#         self.__last_name=ln
#
#     def __init__(self,fn,ln):
#         self.set_first_name(fn)
#         self.set_last_name(ln)
#     def __str__(self):
#         return f'first_name={self.__first_name}, last_name={self.__last_name}'
#
# p=Person('Andrzej','Klusiewicz')
# p.set_first_name(None)
# print(p)
#

#75. Stwórz klasę Samochod od nowa z polami marka, model, rejestracja oraz zaimplementowaną metodą __str__
# i kontstruktorem sparametryzowanym.
# Zadbaj o to by w klasie samochód wszystkie pola były prywatne, ale by istniały metody typu setter służące
# do ustawiania wartości tych pól. Zadbaj o to by wszystkie odwołania wewnątrz klasy do pól były wykonywane
# za pośrednictwem setterów. Zadbaj o to by nie dało się ustawić marki ani modelu o zerowej długości oraz
# o to by długość rejestracji zawsze mieściła się w zakresie 7-8 znaków.
# W przypadku podania niewłasciwych danych rzuć wyjątkiem z adekwatnym komunikatem.
