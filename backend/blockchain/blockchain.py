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

  def replace_chain(self, chain):
    """
    Replace the local chain with the incoming one if the following applies:
      - The incoming chain is longer that the local one.
      - The incoming chain is formatted properly.
    """

    if len(chain) <= len(self.chain):
      raise Exception('Cannot Replace. The incoming chain must be longer')
    
    try:
      Blockchain.is_valid_chain(chain)
    except Exception as e:
      raise Exception(f'Cannot replace. The incoming chain is invalid: {e}')

    self.chain = chain

  def to_json(self):
    serialized_chain = []
    """
    Serialize the blockchain into a list of blocks
    """
    # for block in self.chain:
    #   serialized_chain.append(block.to_json())

    # return serialized_chain

    return list(map(lambda block: block.to_json(), self.chain))


  @staticmethod
  def from_json(chain_json):
    """
    Deserialize a list of serialized blocks into a Blockchain instance.
    The result will contain a chain list of Block instances.
    """
    blockchain = Blockchain()
    blockchain.chain = list(map(lambda block_json: Block.from_json(block_json), chain_json)
    )

    return blockchain
    
  @staticmethod
  def is_valid_chain(chain):
    """
    Validate the incoming chain.
    Rules:
      - chain must start with the genesis block
      - blocks must be formatted correctly
    """


    if chain[0] != Block.genesis():
      raise Exception('The genesis block must be valid')

    for i in range(1, len(chain)):
      block = chain[i]
      last_block = chain[i - 1]
      Block.is_valid_block(last_block, block)


def main():

  blockchain = Blockchain()
  blockchain.add_block('one')
  blockchain.add_block('two')

  
  print(blockchain)
  print(f'blockchain.py __name__: {__name__}')

  

if __name__ == '__main__':
  main()

