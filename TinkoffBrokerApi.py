from datetime import timedelta

from tinkoff.invest import Client
from tinkoff.invest.utils import now
from tinkoff.invest.schemas import CandleInterval

class TinkoffBrokerApi:
    def __init__(self):
        self.client = None
        self.token = ""
        self.coordinator = None

    def set_coordinator(self, coordinator):
        self.coordinator = coordinator

    def set_token(self, token):
        if token is None:
            return
        self.token = token
        self.connect()

    def connect(self):
        pass
        #self.client = Client(self.token)

    def is_connected(self):
        return self.client is not None

    def get_price_info(self):
        data = None
        with Client(self.token) as client:
            data = list(client.get_all_candles(
                figi="BBG004730N88",
                from_=now() - timedelta(days=365),
                interval=CandleInterval.CANDLE_INTERVAL_HOUR,
            ))
        return data

    def buy(self, price):
        self.coordinator.set_buy_info(price)
        pass

    def sell(self, price):
        self.coordinator.set_sell_info(price)
        pass
