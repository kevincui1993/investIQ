import logging

from investiq.dolthub.dolthub_client import DolthubClient


class StockAnalyzer:

    def __init__(self, stock_symbols):
        self.stock_symbols = stock_symbols
        self.logger = logging.getLogger(self.__class__.__name__)
        self.stock_balance_sheets = {}
        self.dolthub_client = DolthubClient()
        self._fetch_stock_data()

    def _fetch_stock_data(self):
        for symbol in self.stock_symbols:
            balance_sheet = self.dolthub_client.fetch_latest_balance_sheet(symbol)
            self.stock_balance_sheets[symbol] = balance_sheet

    def recommend(self):
        scores = {}
        for symbol, balance_sheet in self.stock_balance_sheets.items():
            scores[symbol] = self._score_stock(balance_sheet)

        best_stock = max(scores, key=scores.get)
        return best_stock

    def _score_stock(self, stock_data):
        score = 0
        score += float(stock_data.get('total_assets', 0)) * 0.5
        score += float(stock_data.get('cash_and_equivalents', 0)) * 0.2
        score += float(stock_data.get('receivables', 0)) * 0.15
        score += float(stock_data.get('other_current_assets', 0)) * 0.1
        score += float(stock_data.get('other_current_assets', 0)) * 0.05

        return score
