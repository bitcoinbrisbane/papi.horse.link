#!/usr/bin/env python3
from flask import Flask
from web3 import Web3, HTTPProvider

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

    provider_uri = "https://goerli.infura.io/v3/d92ab3de97fc461f923c45b1edfc1685"
    w3 = Web3(HTTPProvider())
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
