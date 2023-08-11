from flask import Flask, render_template, redirect, url_for
from data import products as product_list

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/products')
def products():
    return render_template('products.html', products=product_list)


from flask import Flask, render_template, redirect, url_for
from data import products as product_list

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/products')
def products():
    return render_template('products.html', products=product_list)


@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = next((item for item in product_list if item['id'] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template('product_detail.html', product=product)


if __name__ == '__main__':
    app.run(debug=True)
