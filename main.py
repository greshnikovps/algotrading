
'''
from datetime import timedelta

TOKEN = "t.SYk8VU-SfWW7WX33_fXX4VOLGHexFrSRYTjT_6ldKVJxmb_UwHElz3VLtYjlrWuch_J4Pj0bq_gY1FuxdttPmQ"

def main():
    with Client(TOKEN) as client:
        for candle in client.get_all_candles(
            figi="BBG004730N88",
            from_=now() - timedelta(days=365),
            interval=CandleInterval.CANDLE_INTERVAL_HOUR,
        ):
            print(candle)

    return 0


if __name__ == "__main__":
    main()
'''

from Coordinator import Coordinator
from TelegramNotifier import TelegramNotifier
from TinkoffBrokerApi import TinkoffBrokerApi
from MarketCache import MarketCache
from AlgorithmicAnalyzer import AlgorithmicAnalyzer
from Config import Config

if __name__ == "__main__":
    config = Config()
    coordinator = Coordinator()

    # set notifier
    tg_notifier = TelegramNotifier()
    coordinator.set_notifier(tg_notifier)

    # set broker API
    tinkoff_api = TinkoffBrokerApi()
    token = config.token()
    tinkoff_api.set_token(token)
    coordinator.set_broker_api(tinkoff_api)

    # set market cache
    market_cache = MarketCache()
    coordinator.set_market_cache(market_cache)

    # set algorithmic analyzer
    alorithmic_analyzer = AlgorithmicAnalyzer()
    coordinator.set_algorithmic_analyzer(alorithmic_analyzer)

    # set loop interval
    coordinator.set_loop_interval_ms(100)  # TODO set interval from config file

    # check if this stratigy is good or bad
    coordinator.test_algorithmic_analyzer()

    # start main loop
    coordinator.start_loop()
