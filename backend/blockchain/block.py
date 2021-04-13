import time

from backend.util.crypto_hash import crypto_hash

GENESIS_DATA = {
  'timestamp': 1,
  'last_hash': 'genesis_last_hash',
  'hash': 'genesis_hash',
  'data': [], 
  'difficulty': 5,
  'nonce': 'genesis_nonce',
}
class Block: 
  """
  Block: A unit of storage.
  Stores transactions in blockchain that supports a cryptocurrency.
  """
  def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
    self.timestamp = timestamp
    self.last_hash = last_hash
    self.hash = hash
    self.data = data
    self.difficulty = difficulty
    self.nonce = nonce

  def __repr__(self): 
    # python special method for string representation
    return (
      'Block('
      f'timestamp: {self.timestamp}, '
      f'last_hash: {self.last_hash}, '
      f'hash: {self.hash}, '
      f'Block - data: {self.data},'
      f'difficulty: {self.difficulty},'
      f'nonce: {self.nonce})'

    )

  @staticmethod
  def mine_block(last_block, data):
    """
    Mine a block based on the given last_block and data, until a block hash
    is found that meets the leading 0's proof of work requirement.
    """
    timestamp = time.time_ns()
    last_hash = last_block.hash
    difficulty = last_block.difficulty
    nonce = 0
    hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

    while hash[0:difficulty] != '0' * difficulty:
      nonce += 1
      timestamp = time.time_ns()
      hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)


    return Block(timestamp, last_hash, hash, data, difficulty, nonce)

  @staticmethod
  def genesis():
    """
    Generates the genesis block.
    """
    # return Block(
    #   GENESIS_DATA['timestamp'],
    #   GENESIS_DATA['gensis_last_hash'],
    #   GENESIS_DATA['hash'],
    #   GENESIS_DATA['data']
    #   added Genesis data for difficulty and nonce
    # )

    return Block(**GENESIS_DATA)
  
def main():
 genesis_block = Block.genesis()
 block = Block.mine_block(genesis_block, 'foo')
 print(block)



if __name__ == '__main__':
  main()
