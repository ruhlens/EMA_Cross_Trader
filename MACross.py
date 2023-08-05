"""
THIS IS A PAPER TRADING PROGRAM BASED ON EMA Crosses
"""

from algorithms import Algorithm
from graph import Graph
import keyboard
from datetime import datetime
from FinnHubData import FinnHubData
from Indicator import Indicator
import time

def unixTime(days):
    """Function to calculate a timeperiod in unix form.
    Args: 
        days(int): the number of days to calculate in unix form 
    Returns:
        days * 86400: the unix form of the days argument
    """
    return days * 86400

def main():
    """Main function to handle the algorithm."""
    print("Golden Cross Trading Algorithm Started. Press 'Q' to Close")
    ticker = "AAPL"
    run = True
    money = 1000
    shares = 0
    x = []
    y = []
    index = 0
    graph = Graph()
    buys = []
    sells = []
    avBuyPrice = 0
    avSellPrice = 0
    percentage = 0
    key = 'FINNHUB API KEY HERE'
    profit = 0
    while run:
        if keyboard.is_pressed("q"):
            run = False
        client = FinnHubData(key)
        timeSeries = client.getCandle(ticker, 'D', int((time.time() - unixTime(365))), int(time.time()))
        time.sleep(1)
        currentPrice = timeSeries.get('c')[-1]
        currentTime = datetime.now().time().strftime("%H:%M:%S")
        emaSmall = Indicator().getEMA(timeSeries.get('c'), 9)
        emaLarge = Indicator().getEMA(timeSeries.get('c'), 50)
        x.append(currentTime)
        y.append(float(f'{currentPrice:.2f}'))
        if len(x) > 20:
            x.remove(x[0])
            graph.clear()
        if len(y) > 20:
            y.remove(y[0])
            graph.clear()
        index += 1
        algo = Algorithm().goldenCross(emaSmall, emaLarge, currentPrice, money, shares)
        orderType = algo[0]
        money = algo[1]
        shares = algo[2]
        price = algo[3]
        percentage = (money - 100000) / 100000
        graph.liveGraph(x,y, shares, avBuyPrice, avSellPrice, percentage, money, emaSmall, emaLarge, price, ticker)
        if orderType == "B":
            buys.append(price)
        if orderType == "S":
            sells.append(price)
        if len(buys) > 0:
            avBuyPrice = sum(buys) / len(buys)
        if len(sells) > 0:
            avSellPrice = sum(sells) / len(sells)
    graph.show()

if __name__ == "__main__":
    main()
