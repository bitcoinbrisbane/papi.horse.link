#!/usr/bin/env python3
from flask import Flask
from web3 import Web3

app = Flask(__name__)


@app.route('/markets/', methods=['GET'])
def welcome():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

