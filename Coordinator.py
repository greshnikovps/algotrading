import time

from constants import *
import matplotlib.pyplot as plt

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
        if not broker_api.is_connected():
            broker_api.connect()

    def set_market_cache(self, market_cache):
        self.market_cache = market_cache

    def set_algorithmic_analyzer(self, algorithmic_analyzer):
        self.algorithmic_analyzer = algorithmic_analyzer

    def set_loop_interval_ms(self, loop_interval_ms):
        self.loop_interval_ms = loop_interval_ms

    def set_buy_info(self, price):
        self.notifier.seng_message("buying with price " + str(price))
        self.shares_balance += 1
        self.cash_balance -= price

    def set_sell_info(self, price):
        self.notifier.seng_message("selling with price " + str(price))
        self.shares_balance -= 1
        self.cash_balance += price

    def test_algorithmic_analyzer(self):
        """
        get prices for all test period from stock market api
        simulate streaming prices info into the algorithmic_analyzer
        get result from the algorithmic_analyzer and calculate income
        """
        self.sum_balance = 100
        self.shares_balance = 0
        self.cash_balance = self.sum_balance

        balances_history = []
        prices_history = []
        shares_num_history = []

        prices_info = self.broker_api.get_price_info()
        for price_info in prices_info:
            if self.algorithmic_analyzer.is_ready_to_calculate():
                result = self.algorithmic_analyzer.calculate_result()
                if result == BUY:
                    self.broker_api.buy(price_info.high.units)
                elif result == SELL:
                    self.broker_api.sell(price_info.high.units)
                self.sum_balance = self.shares_balance * price_info.high.units + self.cash_balance
                balances_history.append(self.sum_balance)
                prices_history.append(price_info.high.units)
                shares_num_history.append(self.shares_balance)

            self.algorithmic_analyzer.add_prices([price_info])

        print("loop ended")
        plt.plot(balances_history)
        plt.show()

        plt.plot(prices_history)
        plt.show()

        plt.plot(shares_num_history)
        plt.show()











