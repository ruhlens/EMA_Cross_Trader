import finnhub

class FinnHubData:
    """Finnhub Data collection class."""

    def __init__(self, key):
        self.key = key
        self.client = finnhub.Client(api_key=self.key)

    def getCandle(self, ticker, resolution, start, end):
        """Returns candlestick data for the given ticker.
        Args:
            ticker(str): the given ticker
            resolution(str): the timeframe for the data (1, 5, 15, 30, 60, D, W, M)
            start(int): unix timestamp for start time 
            end(int): unix timestamp for end time
        Returns:
            self.client.stock_candles(ticker, resolution)
        """
        return self.client.stock_candles(ticker, resolution, start, end)

    def getPrice(self, ticker):
        """Returns the current price of a given ticker.
        Args:
            ticker(str): the given ticker 
        Returns:
            self.client.quote(ticker).get('c')
        """
        return self.client.quote(ticker).get('c')

    def getMACD(self, ticker, start, end, res='D', stype='c', fastperiod=12, slowperiod=26, signalperiod=9):
        """Returns data for a given ticker containing the MACD correlating to the args specified in this format:
            {'c': [], 'h': [], 'l': [], 'o': [], 's': '', 'macd': [], 't': [], 'v': []}.
        Args:
            ticker(str): the given ticker
            start(int): the start date timestamp in unix
            end(int): the end date timestamp in unix
            res(str): the timeframe for the data (1, 5, 15, 30, 60, D, W, M)
            stype(str): the ohlc column to analyze 
            fastperiod(int): the length of the fastperiod to calculate the exponential moving average of
            slowperiod(int): the length of the slowperiod to calculate the exponential moving average of
            signal_period(int): the length of the signal period to calculate the exponential moving average of
        Returns:
            self.client.technical_indicator(symbol=ticker, indicator= 'macd', resolution=res, _from=start,
            to=end, indicator_fields={'seriestype': stype, 'fastperiod': fastperiod,
            'slowperiod': slowperiod, 'signalperiod': signalperiod})
        """
        return self.client.technical_indicator(symbol=ticker, indicator= 'macd', resolution=res, _from=start, to=end, indicator_fields={'seriestype': stype,
                                                                                                   'fastperiod': fastperiod, 'slowperiod': slowperiod,
                                                                                                   'signalperiod': signalperiod})

    def getEMA(self, ticker, start, end, timeperiod, res='D', stype='c'):
        return self.client.technical_indicator(symbol=ticker, indicator= 'ema',
                                               resolution=res, _from=start, to=end, indicator_fields={})

