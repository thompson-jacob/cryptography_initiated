import os
import requests
import random


from flask import Flask, jsonify, request
 

from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub
from backend.wallet.wallet import Wallet
from backend.wallet.transaction import Transaction

app = Flask(__name__)
blockchain = Blockchain()
wallet = Wallet()
pubsub = PubSub(blockchain)



@app.route('/test')
def route_default():
  return 'Welcome to the blockchain app'

@app.route('/blockchain')
def route_blockchain():
  return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
  transaction_data = 'stubbed_transaction_data'

  blockchain.add_block(transaction_data)

  block = blockchain.chain[-1]
  pubsub.broadcast_block(block)
  return jsonify(block.to_json())
  
@app.route('/wallet/transact', methods=['POST'])
def route_wallet_transact():
  transaction_data = request.get_json()
  transaction = Transaction(
    wallet,
    transaction_data['recipient'],
    transaction_data['amount']
    )
  return jsonify(transaction.to_json())


ROOT_PORT = 5000
PORT = ROOT_PORT


if os.environ.get('PEER') == 'True':
  PORT = random.randint(5001, 6000)
  result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
  result_blockchain = Blockchain.from_json(result.json())
  
  # print(f'result.json(): {result.json()}')
  try:
    blockchain.replace_chain(result_blockchain.chain)
    print('\n -- Successfully sychronized the local chain')
  except Exception as e:
    print(f'\n -- Error synchronizing: {e}')
  

app.run(port=PORT)