from constants import *


class AlgorithmicAnalyzer:
    """
    Class contains all required data for calculating result: BUY, SELL or DO_NOTHING. When it gets request to
    advise the deal type, it calculates verdict (or takes from cache) and returns result. When it gets new prices info
    from the stock market it clears the cache.
    """
    def __init__(self):
        self.stock_prices = []
        self.result = None
        self.prices_needed_len = 5  # every child of this class should override this field

    def get_result(self):
        if self.result is None:
            self.calculate_result()

        return self.result

    def is_ready_to_calculate(self):
        return len(self.stock_prices) == self.prices_needed_len

    def add_prices(self, new_prices):
        self.result = None
        self.stock_prices = [*self.stock_prices, *new_prices]

        # if we have not enough information to calculate
        if len(self.stock_prices) < self.prices_needed_len:
            self.result = ERROR
            return

        # if we have too much information about the past
        elif len(self.stock_prices) > self.prices_needed_len:
            self.stock_prices = self.stock_prices[-self.prices_needed_len:]

    def calculate_result(self):
        prices_sum = 0
        for price in self.stock_prices:
            prices_sum += price.high.units

        prices_sum = round(prices_sum)
        if (prices_sum % 2) != 0:
            self.result = BUY
        else:
            self.result = SELL

        return self.result
