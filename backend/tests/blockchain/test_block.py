from backend.blockchain.block import Block, GENESIS_DATA

def test_mine_block():
  last_block = Block.genesis()
  data = 'test-data'
  block = Block.mine_block(last_block, data)


  assert isinstance(block, Block) 
  assert block.data == data
  assert block.last_hash == last_block.hash


def test_genesis():
  genesis = Block.genesis()


  # assert isinstance(genesis, Block)
  # assert genesis.timestamp == GENESIS_DATA['timestamp']
  # assert genesis.last_hash == GENESIS_DATA['last_hash']
  # assert genesis.hash == GENESIS_DATA['hash']
  # assert genesis.data == GENESIS_DATA['data']

 #refactored with a for loop, using the key and value of genesis
 #by creating a get attribute and assigning genesis to the value of key

 #additional print statements can be seen by running the 
 # -rP flag for passed tests || -rx flag for failed tests
 #  pytest -rP                  pytest -rx

  print(GENESIS_DATA.items())
  for key, value in GENESIS_DATA.items():
    getattr(genesis, key) == value
    # print(getattr(genesis, key))





  