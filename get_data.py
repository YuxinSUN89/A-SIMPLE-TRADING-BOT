#------ IMPORT LIBRARY and CONFIG -------#

import Yuxin_config
import pandas as pd
pd.options.display.max_rows = 999
pd.set_option('display.max_columns', None)

from pytz import timezone
tz = timezone('EST')


class StockInfo(object):
    def __init__(self, symbols, rate, slow, fast):
        self.symbols = symbols
        self.rate = rate
        self.slow = slow
        self.fast = fast

    def get_minute_bar(self):
        # Add Position Info #
        ticker = [x.symbol for x in Yuxin_config.api.list_positions()]
        qty = [x.qty for x in Yuxin_config.api.list_positions()]
        avg_entry_price = [x.avg_entry_price for x in Yuxin_config.api.list_positions()]
        my_position = dict(zip(ticker, qty))
        entry_price = dict(zip(ticker, avg_entry_price))
        data = Yuxin_config.api.get_barset(self.symbols, self.rate, limit=20).df

        # CONSTRUCT STOCK DATAFRAME INFO HERE
        for x in self.symbols:

            data.loc[:, (x, 'fast_ema_1min')] = data[x]['close'].rolling(window=self.fast).mean()
            data.loc[:, (x, 'slow_ema_20min')] = data[x]['close'].rolling(window=self.slow).mean()
            data.loc[:, (x, 'return_1_min')] = (data[x]['close'] - data[x]['close'].shift(1)) / \
                                               (data[x]['close'].shift(1))
            data.loc[:, (x, 'loading')] = int(Yuxin_config.loading[x])
            if x in ticker:
                data.loc[:, (x, 'qty')] = int(my_position[x])

            else:
                data.loc[:, (x, 'qty')] = 0

        return data

    def get_signals(self):
        data = self.get_minute_bar()
        signals = {}
        # CONSTRUCT SIGNALS HERE
        for x in self.symbols:

            if (data[x].iloc[-1]['fast_ema_1min'] >= data[x].iloc[-1]['slow_ema_20min']):
                signal = (data[x].iloc[-1]['loading'])

            # Sell-out signal - number of shares to be liquidated is the value of signal
            else:
                signal = 0
            signals[x] = signal

        return signals

if __name__ == '__main__':
    # ------ GET STOCK DATAFRAME -----#
    stock_data = StockInfo(Yuxin_config.symbols, Yuxin_config.freq, Yuxin_config.slow, Yuxin_config.fast)
    dataframe = stock_data.get_minute_bar()

    #------ GET TRADING SIGNALS -----#
    trading_signal = stock_data.get_signals()
    print(dataframe)


