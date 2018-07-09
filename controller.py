from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

URL = 'http://localhost:8080/api/'


@app.route('/')
def root():
    return render_template('homepage.html')


@app.route('/sellers', methods=['GET', 'POST'])
def sellers():
    if request.method == 'GET':
        return render_template('register_seller.html')
    else:
        dict = request.form
        response = requests.post(url=URL + 'sellers', data=dict)
        return jsonify(response.json())


@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return render_template('register_product.html')
    else:
        dict = request.form
        response = requests.post(url=URL + 'products', data=dict)
        return jsonify(response.json())


@app.route('/stores', methods=['GET', 'POST'])
def stores():
    if request.method == 'GET':
        return render_template('register_store.html')
    else:
        dict = request.form
        response = requests.post(url=URL+'store', data=dict)
        return jsonify(response.json())


@app.route('/seller_get', methods=['GET', 'POST'])
def sellers_get():
    if request.method == 'GET':
        return render_template('consulta.html', item='seller')
    else:
        dict = request.form
        response = requests.get(url=URL + 'sellers/' + dict['id'])
        return jsonify(response.json())


@app.route('/product_get', methods=['GET', 'POST'])
def products_get():
    if request.method == 'GET':
        return render_template('consulta.html', item='product')
    else:
        dict = request.form
        response = requests.get(url=URL + 'products/' + dict['id'])
        return jsonify(response.json())


@app.route('/store_get', methods=['GET', 'POST'])
def stores_get():
    if request.method == 'GET':
        return render_template('consulta.html', item='store')
    else:
        dict = request.form
        response = requests.get(url=URL + 'stores/' + dict['id'])
        return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)
