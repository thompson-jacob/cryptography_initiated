import hashlib
import json


def crypto_hash(*args):
  """
  Return a sha-256 hash of the given arguments.
  """

  stringified_args = map(lambda data: json.dumps(data), args)
  print(f'stringified_args: {stringified_args}')
  joined_data = ''.join(stringified_args)
  print(f'joined_data: {joined_data}')

  # print(hashlib.sha256(stringified_data.encode('utf-8')).hexdigest())
  return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()
  # data must be encoded into a utf-8 using a hexdigest to return a string, 
  # however this data needs to be stringifired by importing json and addings the data into a json.dumps(data) variable

def main():
  print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")

if __name__ == '__main__':
  main()
