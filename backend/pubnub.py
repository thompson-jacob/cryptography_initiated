from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from config import subscriber_key, publisher_key



pnconfig = PNConfiguration()
pnconfig.subscribe_key = config.subscriber_key
pnconfig.publish_key = config.publisher_key
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

pubnub.publish().channel(TEST_CHANNEL).message({ 'foo': 'bar'}).sync()

pubnub.add_listener(SubscribeCallback)

if __name__ == '__main__':
  main()

