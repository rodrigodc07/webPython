from flask import Flask, jsonify, render_template, request, flash, url_for
import requests
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "super secret key"

URL = 'http://localhost:8080/api/'


def status_code_parser(status_code):
    if status_code == 200:
        return 'Sucesso'
    elif status_code == 201:
        return 'Criado com Sucesso'
    elif status_code == 404:
        return 'Cadastro não encontrado'
    elif status_code == 422:
        return 'Parametro Invalido'


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
        response = requests.post(url=URL + 'store', data=dict)
        return jsonify(response.json())


@app.route('/seller_get', methods=['GET', 'POST'])
def seller_get():
    if request.method == 'GET':
        return render_template('consulta.html', item='seller')
    else:
        dict = request.form
        response = requests.get(url=URL + 'sellers/' + dict['id'])
        if (response.status_code == 200):
            return jsonify(response.json())
        else:
            flash(status_code_parser(response.status_code), 'error')
            return redirect(url_for('seller_get'))


@app.route('/product_get', methods=['GET', 'POST'])
def product_get():
    if request.method == 'GET':
        return render_template('consulta.html', item='product')
    else:
        dict = request.form
        response = requests.get(url=URL + 'products/' + dict['id'])
        if (response.status_code == 200):
            return jsonify(response.json())
        else:
            flash(status_code_parser(response.status_code), 'error')
            return redirect(url_for('product_get'))


@app.route('/store_get', methods=['GET', 'POST'])
def store_get():
    if request.method == 'GET':
        return render_template('consulta.html', item='store')
    else:
        dict = request.form
        response = requests.get(url=URL + 'stores/' + dict['id'])
        if (response.status_code == 200):
            return jsonify(response.json())
        else:
            flash(status_code_parser(response.status_code), 'error')
            return redirect(url_for('store_get'))


if __name__ == "__main__":
    app.run(debug=True)
