class Block: 
  """
  Block: A unit of storage.
  Stores transactions in blockchain that supports a cryptocurrency.
  """
  def __init__(self, data):
    self.data = data

  def __repr__(self): 
    # python
    return f'Block - data: {self.data}'

class Blockchain:
  """
  Blockchain: A public ledger of transactions.
   This is implemented as a list of blocks - data sets of transactions
  """

  def __init__(self):
    self.chain = []

  def add_block(self, data): 
    self.chain.append(Block(data))
    # appends the newly instantiated Block to the Blockchain 'chain'

  def __repr__(self):
    return f'Blockchain: {self.chain}'

blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')


print(blockchain)
