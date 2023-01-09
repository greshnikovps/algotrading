TOKEN = "t.SYk8VU-SfWW7WX33_fXX4VOLGHexFrSRYTjT_6ldKVJxmb_UwHElz3VLtYjlrWuch_J4Pj0bq_gY1FuxdttPmQ"  # sandbox token

from tinkoff.invest import Client
from tinkoff.invest.utils import now

class TinkoffBrokerApi:
    def __init__(self):
        self.client = None
        self.token = ""

    def set_token(self, token):
        if token is None:
            return
        self.token = token

    def connect(self):
        self.client = Client(self.token)

    def is_connected(self):
        return self.client is not None

    def get_current_price(self):
        last_price = ()
