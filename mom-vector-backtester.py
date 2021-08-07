#
# Python Module with Class for Vectorized Backtesting of Momentum-based Strategies
#

import numpy as np
import pandas as pd

class MomVectorBacktester(object):
    ''' Class for the vectorized backtesting of momentum-based trading strategies

    Attributes
    ----------
    symbol: str             RIC (financial instrument) to work with
    start: str              start date for data selection
    end: str                end date for data selection
    amount: int, float      amount to be invested at the beginning
    tc: float               proportional transaction costs (e.g., 0.5% = 0.005) per trade

    Methods
    ---------
    get_data:               retrieves and prepares the base data set
    run_strategy:           runs the backtest for the momentum-based strategy
    plot_results:           plots the performance of the strategy compared to the symbol
    ''''

    def __init__(self, symbol, start, end, amount, tc):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.amount = amount
        self.tc = tc
        self.results = None
        self.get_data()

    def get_data(self):
        ''' Retrieves and prepares the data. '''

        raw = pd.read_csv('http://hilpisch.com/pyalgo_eikon_eod_data.csv',
            index_col = 0, parse_dates = True).dropna()
        raw = pd.DataFrame(raw[self.symbol])
        raw = raw.loc[self.start:self.end]
        raw.rename(columns={self.symbol: 'price'}, inplace = True)
        raw['return'] = np.log(raw / raw.shift(1))
        self.data = raw