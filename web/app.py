from flask import Flask, render_template
from domain import *

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    #return '<h1>Strona główna</h1>'
    return render_template("index.html")

@app.route('/show_products')
def show_products():
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

class Favourites:
    film=None
    book=None

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
