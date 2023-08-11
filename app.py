from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.get("/products")
def products():
    return 'This is the products route'


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
