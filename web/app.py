from flask import Flask, render_template,jsonify
from domain import *
import dao.employees_dao as edao
import dao.products_dao as pdao

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    #return '<h1>Strona główna</h1>'
    return render_template("index.html")

@app.route('/show_products')
def show_products():
    for p in pdao.get_all():
        print(p)
    return render_template("show_products.html")

@app.route('/about')
def about():
    #a=Author()
    # # a.first_name="Andrzej"
    # # a.last_name='Klusiewicz'
    # # a.phone_number='112'
    # # a.email='klusiewicz@jsystems.pl'
    a=Author("Andrzej","Klusiewicz",'112','klusiewicz@jsystems.pl')
    print(a)
    return render_template("about.html",author=a)

@app.route('/show_employees')
def show_employees():
    employees=edao.get_all()
    for e in employees:
        print(e)
    return render_template("show_employees.html",employees=employees)

@app.route('/tests')
def tests():
    jezyki=['python','java','pl/sql','pl/pgsql']
    f=Favourites()
    f.film='Samsara'
    f.book='Organizacje wykładnicze'
    return render_template("tests.html",first_name="Andrzej",last_name="Klusiewicz",langs=jezyki,favourites=f)


if __name__ == '__main__':
    app.run(debug=True,port=80)

#53. Zadbaj o to by Twoja aplikacja miala podstrony : / (strona glowna), /show_products, /about
# Na każdej stronie powinien pojawic sie napis okreslajacy na jakiej stronie jestesmy.
# Włacz tryb debug i zmien port na 80

#54. Zadbaj o to by wszystkie ekrany zamiast zwracac html w returnie zwracaly pliki html
#kazdy ekran powinien miec swoj plik html

#55. Dodaj wszędzie menu

#flask page templates

#przerwa do 14:40

#56. W osobnym module o nazwie domain.py umieść klasę Author
#Klasa ta ma posiadać pola first_name,last_name,email,phone_number
#W kontrolerze ekranu "/about" stwórz obiekt klasy Author, zapelnij go danymi
#i wyświetl te dane na ekranie /about


#57. Do klasy Author dodaj konstruktor sparametryzowany który umożliwi nam tworzenie obiektu
#z podaniem od razu danych. Przerób kontroler widoku /about w taki sposób by
# wykorzystać nowy konstruktor. Zadbaj też o to by przy wejsciu na ekran wyswietlila
#się na konsoli zawartosc przekazywanego obiektu.

#58. Stwórz klasę Product o odpowiednich polach - zgodnych z kolumnami w tabelce products.
#Dodaj products_dao i umieść w nim funkcję zwracającą 3 przykładowe obiekty klasy Product.
#Zadbaj o to by po wejściu w /show_products na konsoli wyświetliły się odebrane z dao obiekty.


#59. Wyświetl pochodzące z dao dane o produktach na widoku. Wyswietl tylko id produktu,
#produkt i nazwę. Opis będzie widoczny w ekranie szczegoly produktu.