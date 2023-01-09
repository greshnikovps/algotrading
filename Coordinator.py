import time

MS_IN_SEC = 1000


class Coordinator:
    def __init__(self):
        self.loop_interval_ms = None
        self.notifier = None
        self.broker_api = None
        self.algorithmic_analyzer = None
        self.market_cache = None

    def start_loop(self):
        if self.broker_api is None or self.algorithmic_analyzer is None:
            raise Exception("Try to run the loop for not initialized Coordinator")

        #while True:
        #    cur_price = self.broker_api.get_current_price()
        #    print(cur_price)
        #    print("another iteration is done")
        #    time.sleep(self.loop_interval_ms / MS_IN_SEC)

        # or

        # connect callback to self.broker_api streaming
        # if callback method call algorithmic_analyzer.add_prices and algorithmic_analyzer.get_result
        # check result and make a deal if needed

    def set_notifier(self, notifier):
        self.notifier = notifier

    def set_broker_api(self, broker_api):
        self.broker_api = broker_api

    def set_market_cache(self, market_cache):
        self.market_cache = market_cache

    def set_algorithmic_analyzer(self, algorithmic_analyzer):
        self.algorithmic_analyzer = algorithmic_analyzer

    def set_loop_interval_ms(self, loop_interval_ms):
        self.loop_interval_ms = loop_interval_ms

    def test_algorithmic_analyzer(self):
        """
        get prices for all test period from stock market api
        simulate streaming prices info into the algorithmic_analyzer
        get result from the algorithmic_analyzer and calculate income
        """
        pass


