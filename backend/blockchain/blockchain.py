from backend.blockchain.block import Block

class Blockchain:
  """
  Blockchain: A public ledger of transactions.
   This is implemented as a list of blocks - data sets of transactions
  """

  def __init__(self):
    self.chain = [Block.genesis()]

  def add_block(self, data): 
    self.chain.append(Block.mine_block(self.chain[-1], data))
    # appends the newly instantiated Block to the Blockchain 'chain'

  def __repr__(self):
    return f'Blockchain: {self.chain}'

def main():

  blockchain = Blockchain()
  blockchain.add_block('one')
  blockchain.add_block('two')

  
  print(blockchain)
  print(f'blockchain.py __name__: {__name__}')

  

if __name__ == '__main__':
  main()