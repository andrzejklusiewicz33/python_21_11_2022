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
#
# class Samochod:
#
#     def set_marka(self,ma):
#         if ma is None or len(ma)==0:
#             raise Exception('marka nie może być pusta')
#         self.__marka = ma
#
#     def set_model(self,mo):
#         if mo is None or len(mo)==0:
#             raise Exception('model nie może być pusty')
#         self.__model = mo
#
#     def set_rejestracja(self,re):
#         if re is None or len(re)>8 or len(re)<7:
#             raise Exception('długość rejestracji musi mieć 7-8 znaków')
#         self.__rejestracja = re
#     def __init__(self,ma,mo,re):
#         self.set_marka(ma)
#         self.set_model(mo)
#         self.set_rejestracja(re)
#     def __str__(self):
#         return f"marka={self.__marka}, model={self.__model}, rejestracja={self.__rejestracja}"
#
# s=Samochod('A','B','1234567')
# print(s)

# class Samochod:
#     def jedz(self):
#         print('łutututututu')
#
# class SuperSamochod(Samochod):
#     def turbo(self):
#         print('turbo!!!!!!!')
#
# s=Samochod()
# s.jedz()
# ss=SuperSamochod()
# ss.jedz()
# ss.turbo()
#
#
# class A:
#     def funkcjaA(self):
#         print('funkcja z a')
#
#
# class B:
#     def funkcjaB(self):
#         print('funkcja z b')
#
# class C(A,B):
#     pass
#
# a=A()
# a.funkcjaA()
# b=B()
# b.funkcjaB()
# c=C()
# c.funkcjaA()
# c.funkcjaB()

#
#
# class A:
#     def funkcja(self):
#         print('funkcja z a')
#
# class B:
#     def funkcja(self):
#         print('funkcja z b')
#
# class C(B,A):
#     pass
#
# c=C()
# c.funkcja()

#76. Stwórz klasę Samochod i dodaj do niej metodę jedz() która bedzie wyświetlala napis na konsoli.
# Dodaj konstruktor pozwalajacy tworzyc obiekty z podaniem marki modelu i rejestracji do klasy Samochod.
# Stwórz klasę "Działo" która będzie posiadała metodę strzelaj(). Stwórz klasę "Czolg" która będzie
# dziedziczyła po klasach Samochod i Dzialo. Stwórz obiekt klasy Czolg i wywolaj na nim zarówno metodę jedz()
# jak i strzelaj(). Zwróć uwagę na to jak trzeba wywołać konstruktor obiektu klasy Czolg.
# Sprawdz czy zmiana kolejnosci dziedziczenia wplywa na sposob wywołania konstruktora.
# Sprawdz czy dodanie bezparametrowego __init__ do klasy Czolg zmienia zachowanie.
#
#
# class Samochod:
#     def jedz(self):
#         print('popierdzielam....')
#     def __init__(self,ma,mo,re):
#         self.marka=ma
#         self.model=mo
#         self.rejestracja=re
#
# class Dzialo:
#     def strzelaj(self):
#         print('jeb jeb jeb z dzidy laserowej')
#     #
#     # def __init__(self):
#     #     pass
#
# class Czolg(Samochod,Dzialo):
#     def __init__(self):
#         super().__init__('a','b','c')
#         print('dodatkowe czynnosci')
#
#
# c=Czolg()
#
# from abc import ABC,abstractmethod
# class AbstractDao(ABC):
#     @abstractmethod
#     def get_all(self):
#         pass
#
# class OracleDao(AbstractDao):
#     def get_all(self):
#         return ['dane','z','oracle','dao']
#
# class PostgresDao(AbstractDao):
#     def get_all(self):
#         return ['dane', 'z', 'postgresql', 'dao']
#
#
# odao=OracleDao()
# pdao=PostgresDao()
#
#
# class Komponent:
#     def __init__(self,dao:AbstractDao):
#         self.dao=dao
#     def some_process(self):
#         for e in self.dao.get_all():
#             print(e)
# #
# #dao=OracleDao()
# dao=PostgresDao()
# #k=Komponent(dao)
# k=Komponent(dao)
# k.some_process()




#77. Stwórz klasę abstrakcyjną Restauracja która będzie posiadała abstrakcyjną metodę "serwuj_danie".
# Stwórz klasy "RestauracjaChinska", "RestauracjaWloska" i "RestaruracjaPolska". Wymuś posiadanie implementacji
# metody abstrakcyjnej "serwuj_danie" we wszystkich tych klasach ale o różnej implementacji.
# Powołaj do życia obiekty tych klas, a następnie na rzecz każdego z tych obiektów wywołaj funkcję serwuj_danie.
#
# from abc import ABC, abstractmethod
# class Restauracja(ABC):
#     @abstractmethod
#     def serwuj_danie(self):
#         pass
#
# class RestauracjaChinska(Restauracja):
#     def serwuj_danie(self):
#         print('niepokojącowe szczekanie z kuchni')
#
# class RestauracjaWloska(Restauracja):
#     def serwuj_danie(self):
#         print('pizza, makaron i co tam jeszcze')
#
# class RestauracjaPolska(Restauracja):
#     def serwuj_danie(self):
#         print('lorneta z meduzą')
#
# #rc=RestauracjaChinska()
#
# restauracje=[RestauracjaChinska(),RestauracjaWloska(),RestauracjaPolska()]
# for r in restauracje:
#     r.serwuj_danie()

