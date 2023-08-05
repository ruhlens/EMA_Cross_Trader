class Indicator:
    """Indicator class for manually calculating indicators."""

    def __init__(self):
        pass 

    def getEMA(self, timeSeries, timeperiod):
        """Returns the EMA for the most recent point in a timeseries (assuming the most recent point is index -1).
        Args:
            timeSeries(list): the time series to analyze
            timeperiod(int): the timeperiod to calculate the EMA for
        Returns:
            int: the ema for the most recent point in the given timeseries
        """
        if len(timeSeries) == 0:
            return 0
        EMA = timeSeries[0]
        previousEMA = timeSeries[0]
        for i in range(len(timeSeries)):
            smoothing = 2 / (1 + timeperiod)
            currentPrice = timeSeries[i]
            EMA = (currentPrice * smoothing) + (previousEMA * (1 - smoothing))
            previousEMA = EMA
        return EMA
