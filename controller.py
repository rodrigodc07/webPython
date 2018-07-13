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
        return 'Cadastro nao encontrado'
    elif status_code == 422:
        return 'Parametro Invalido'


def field_parser(field):
    if field == 'name':
        return 'Nome'
    elif field == 'info':
        return 'Informacoes'
    elif field == 'department':
        return 'Departamento'
    elif field == 'sellerName':
        return 'Nome do Seller'
    elif field == 'address':
        return 'Endereco'
    elif field == 'stock':
        return 'Produtos Vendidos'
    elif field == '_id':
        return 'Identificador'


def list_handler(dict,val):
    keys = dict.keys()
    newdict = {val: []}
    for key in keys:
        if val in key:
            newdict[val].append(dict[key])
        else:
            newdict[key] = dict[key]
    return newdict


@app.route('/', methods=['GET', 'POST'])
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
        products_list = requests.get(url=URL + 'products').json()
        sellers_list = requests.get(url=URL + 'sellers').json()
        return render_template('register_store.html', products=products_list, sellers=sellers_list)
    else:
        dict = list_handler(request.form,'stock')
        response = requests.post(url=URL + 'stores', data=dict)
        return jsonify(response.json())


@app.route('/seller_get', methods=['GET', 'POST'])
def seller_get():
    if request.method == 'GET':
        return render_template('consulta.html', item='seller')
    else:
        dict = request.form
        response = requests.get(url=URL + 'sellers/' + dict['id'])
        if (response.status_code == 200):
            return render_template('register_seller.html', data=response.json(), field_parser=field_parser)
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
            return render_template('register_product.html', data=response.json(), field_parser=field_parser)
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
            return render_template('register_store.html', data=response.json(), field_parser=field_parser)
        else:
            flash(status_code_parser(response.status_code), 'error')
            return redirect(url_for('store_get'))


if __name__ == "__main__":
    app.run(debug=True)
