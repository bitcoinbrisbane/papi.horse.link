#!/usr/bin/env python3
from flask import Flask
from web3 import w3

app = Flask(__name__)


def getMarketAddresses():
    registry_address = "0x885386d140e4321102dc218060Bbd55a8B020F4C"
    registry_abi = [
        {
            "inputs": [],
            "name": "marketCount",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "name": "markets",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]

    registry = w3.eth.contract(address=registry_address, abi=registry_abi)
    count = registry.functions.marketCount().call()

    addresses = []

    for i in range(count):
        addresses.append(registry.functions.markets(i).call())


    return addresses


@app.route('/markets/', methods=['GET'])
def welcome():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
