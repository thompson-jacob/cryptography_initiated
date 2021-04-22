import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from backend.config import subscriber_key, publisher_key


pnconfig = PNConfiguration()
pnconfig.subscribe_key = subscriber_key
pnconfig.publish_key = publisher_key

TEST_CHANNEL = 'TEST_CHANNEL'


class Listener(SubscribeCallback):
  def message(self, pubnub, message_object):
    print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')


class PubSub():
  """
  Handles the publish/subscribe layer of the application.
  Provides communication between the nodes of the blockchain network.
  """
  def __init__(self):
    self.pubnub = PubNub(pnconfig)
    self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
    self.pubnub.add_listener(Listener())

  def publish(self, channel, message):
    """
    Publish the message object to the channel.
    """
    self.pubnub.publish().channel(channel).message(message).sync()
    

def main():
  pubsub = PubSub()

  time.sleep(1/2)

  # pubnub.publish(TEST_CHANNEL, message).channel().message({ 'foo': 'bar'}).sync()
  pubsub.publish(TEST_CHANNEL, { 'foo': 'bar'})


if __name__ == '__main__':
  main()

