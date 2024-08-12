import json
import logging

import requests


class DolthubClient:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def fetch_latest_balance_sheet(self, symbol: str):
        url = (
            f"https://www.dolthub.com/api/v1alpha1/post-no-preference/earnings/master?q=SELECT+*%0AFROM+%60balance_sheet_assets"
            f"%60%0AWHERE++%60act_symbol%60+%3D+%27{symbol}%27%0AORDER+BY+%60date%60+DESC%2C+%60act_symbol%60+ASC%2C+%60period%60+ASC%0ALIMIT+1%3B%0A")

        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text).get('rows', [])[0]
        else:
            self.logger.error(f"Failed to fetch balance sheet for symbol {symbol}")
            data = None

        return data
