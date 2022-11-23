from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'Hello World!'

@app.route('/help')
def help():
    return "<h1>Strona pomocy</h1>"

if __name__ == '__main__':
    app.run(debug=True,port=80)

#53. Zadbaj o to by Twoja aplikacja miala podstrony : / (strona glowna), /show_products, /about
# Na każdej stronie powinien pojawic sie napis okreslajacy na jakiej stronie jestesmy
