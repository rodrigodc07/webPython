from flask import Flask, jsonify ,render_template
import requests

app = Flask(__name__)

URL = 'http://localhost:8080/api/'


@app.route('/sellers')
def sellers():
    seller_URL = URL + 'sellers'
    r = requests.get(url=seller_URL)
    # extracting data in json format
    aux = jsonify(r.json())
    return render_template('register_seller.html')


@app.route('/products')
def products():
    products_URL = URL + 'products'
    r = requests.get(url=products_URL)
    # extracting data in json format
    aux = jsonify(r.json())
    return render_template('register_product.html')


@app.route('/stores')
def stores():
    stores_URL = URL + 'stores'
    r = requests.get(url=stores_URL)
    # extracting data in json format
    aux = jsonify(r.json())
    return render_template('register_store.html')

if __name__ == "__main__":
    app.run(debug=True)
