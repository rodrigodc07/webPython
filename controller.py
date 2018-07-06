from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL = 'http://localhost:8080/api/sellers/'


@app.route('/')
def root():
    # sending get request and saving the response as response object
    r = requests.get(url=URL)
    # extracting data in json format
    return jsonify(r.json())


if __name__ == "__main__":
    app.run(debug=True)
