import pytest

from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet

def test_transaction():
  sender_wallet = Wallet()
  recipient = 'Test Wallet'
  amount = 50
  transaction = Transaction(sender_wallet, recipient, amount)

  assert transaction.output[recipient] == amount
  assert transaction.output[sender_wallet.address] == sender_wallet.balance - amount
  
  assert 'timestamp' in transaction.input 
  assert transaction.input['amount'] == sender_wallet.balance
  assert transaction.input['address'] == sender_wallet.address
  assert transaction.input['public_key'] == sender_wallet.public_key

  assert Wallet.verify(
    transaction.input['public_key'],
    transaction.output,
    transaction.input['signature']
  )

def test_transaction_exceeds_balance():
  with pytest.raises(Exception, match='Amount exceeds balance'):
    Transaction(Wallet(), 'testwallet', 1039)

def test_transaction_update_exceeds_balance():
  sender_wallet = Wallet()
  transaction = Transaction(sender_wallet, 'recipient', 69)

  with pytest.raises(Exception, match='Amount exceeds balance'):
    transaction.update(sender_wallet, 'new_recipient', 9001)

def test_transaction_update():
  sender_wallet = Wallet()
  first_recipient = 'first_recipient'
  first_amount = 69

  transaction = Transaction(sender_wallet, first_recipient, first_amount)

  next_recipient = 'next_recipient'
  next_amount = 75
  transaction.update(sender_wallet, next_recipient, next_amount)

  assert transaction.output[next_recipient] == next_amount
  assert transaction.output[sender_wallet.address] == sender_wallet.balance - first_amount - next_amount
  assert Wallet.verify(
    transaction.input['public_key'],
    transaction.output,
    transaction.input['signature']
  )

  first_amount_sent_again_same_sender = 25
  transaction.update(sender_wallet, first_recipient, first_amount_sent_again_same_sender)
  assert transaction.output[first_recipient] == first_amount + first_amount_sent_again_same_sender
  assert transaction.output[sender_wallet.address] == \
    sender_wallet.balance - first_amount - next_amount - first_amount_sent_again_same_sender
  assert Wallet.verify(
    transaction.input['public_key'],
    transaction.output,
    transaction.input['signature']
  )

def test_valid_transaction():
  Transaction.is_valid_transaction(Transaction(Wallet(), 'recipient', 33))

def test_valid_transaction_w_bad_output():
  sender_wallet = Wallet()
  transaction = Transaction(sender_wallet, 'recipient', 50)
  transaction.output[sender_wallet.address] = 8934

  with pytest.raises(Exception, match='Invalid transaction output values'):
    Transaction.is_valid_transaction(transaction)

def test_valid_transaction_w_bad_signature():
  transaction = Transaction(Wallet(), 'recipient', 50)
  transaction.input['signature'] = Wallet().sign(transaction.output)
  with pytest.raises(Exception, match='Invalid signature'):
    Transaction.is_valid_transaction(transaction)