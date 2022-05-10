import requests


TEST_BASE_URL = 'https://testnet.binance.vision/api'
TEST_BASE_WS_URL = 'wss://testnet.binance.vision/ws'
TEST_BASE_STREAM_URL = 'wss://testnet.binance.vision/stream'


class Client:

    def __init__(self, base_url=TEST_BASE_URL):
        self.base_url = base_url
    

    def get(self, endpoint, params=None):
        url = "".join([self.base_url, endpoint])
        print(url)
        return requests.get(url)


    
