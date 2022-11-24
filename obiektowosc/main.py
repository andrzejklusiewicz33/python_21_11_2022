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

class Samochod:
    marka=None
    model=None
    rejestracja=None
    def wyswietl(self):
        print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')
