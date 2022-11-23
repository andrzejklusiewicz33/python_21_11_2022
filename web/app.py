from flask import Flask, render_template

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
    return render_template("about.html")

@app.route('/tests')
def tests():
    return render_template("tests.html")

if __name__ == '__main__':
    app.run(debug=True,port=80)

#53. Zadbaj o to by Twoja aplikacja miala podstrony : / (strona glowna), /show_products, /about
# Na każdej stronie powinien pojawic sie napis okreslajacy na jakiej stronie jestesmy.
# Włacz tryb debug i zmien port na 80

#54. Zadbaj o to by wszystkie ekrany zamiast zwracac html w returnie zwracaly pliki html
#kazdy ekran powinien miec swoj plik html

#55. Dodaj wszędzie menu