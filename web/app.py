from flask import Flask, render_template,request
from domain import *
import dao.employees_dao as edao
import dao.products_dao as pdao
import threading
import time

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    #return '<h1>Strona główna</h1>'
    return render_template("index.html")

@app.route('/show_products')
def show_products():
    products=pdao.get_all()
    for p in products:
        print(p)
    return render_template("show_products.html",products=products)

@app.route('/show_product_details')
def show_product_details():
    id=request.args.get('id')
    print(f'id={id}')
    return render_template("show_product_details.html")

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
    return render_template("show_employees.html",employees=employees)

@app.route('/show_employee_details')
def show_employee_details():
    id=request.args.get('id')
    employee=edao.get_one(id)
    return render_template("show_employee_details.html",employee=employee)

@app.route('/tests')
def tests():
    jezyki=['python','java','pl/sql','pl/pgsql']
    f=Favourites()
    f.film='Samsara'
    f.book='Organizacje wykładnicze'
    t=threading.Thread(target=watek,args=(10,))
    t.start()
    return render_template("tests.html",first_name="Andrzej",last_name="Klusiewicz",langs=jezyki,favourites=f)


def watek(x):
    for i in range(1,x+1):
        time.sleep(1)
        print(i)


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

#60. Przerób widok listy produktów tak, by dane pochodzily z bazy

#61. Dodaj ekran szczegółów produktu i prowadzące do niego linki z listy produktow.
#Po wejsciu na ekran szczegolow produktu na konsoli powinno sie wyswietlic id odczytane z paska

#przerwa  na reklamy do 10:30

#62. Zadbaj o to by strona szczegolow produktu wyswietlala dane z bazy