class Algorithm:
    """Algorithms class."""

    def __init__(self):
        pass

    def RSI(self, rsi, sellTrigger, buyTrigger, price, money, shares):
        """RSI based algorithm that triggers when RSI reaches indicated points.
        Args:
            rsi(float): The current rsi score
            sellTrigger(float): selling point in terms of rsi
            buyTrigger(float): selling point in terms of rsi
            price(float): current price
            money(float): user's current cash
            shares(int): total number of shares

        Returns:
            (list): containing the user's current amount of money and the shares
        """
        price = float(price)
        if price <= money:
            if self.indicator <= buyTrigger:
                print(self.indicator)
                money -= price
                shares += 1
                return ['B', money, shares, price]
        if shares > 0:
            if self.indicator >= sellTrigger:
                money += price
                shares -= 1
                return ['S', money, shares, price]
        return ['n', money, shares, price]

    def MACD(self, macd, sellTrigger, buyTrigger, price, money, shares):
        """MACD based algorithm that triggers when MACD reaches indicated points.
        Args:
            macd(float): the MACD value at the current point
            sellTrigger(float): selling point in terms of MACD
            buyTrigger(float): selling point in terms of MACD
            price(float): current price
            money(float): user's current cash
            shares(int): total number of shares

        Returns:
            (list): containing the user's current amount of money and the shares
        """
        if macd > buyTrigger:
            if price < money:
                money -= price 
                shares += 1
                return ['B', money, shares, price]
        elif macd < sellTrigger:
            if shares > 0:
                money += price 
                shares -= 1 
                return ['S', money, shares, price]
            pass
        return ['n', money, shares, price]

    def goldenCross(self, maSmall, maLarge, price, money, shares):
        """Golden Cross based algorithm that makes decisions based on Golden and Death crosses. 
        Args:
            maSmall(float): the small period moving average
            maLarge(float): the large period moving average
            price(float): current price
            money(float): the user's current cash
            shares(int): total number of shares
        Returns:
            (list): containing the user's current amount of money and the shares
        """
        if maSmall > maLarge:
            #Bull
            if price < money:
                money -= price 
                shares += 1
                return ['B', money, shares, price]
        elif maSmall < maLarge:
            #Bear
            if shares > 0:
                money += price 
                shares -= 1 
                return ['S', money, shares, price]
            pass
        return ['n', money, shares, price]