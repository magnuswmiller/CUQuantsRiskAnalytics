# Stock class object
'''
Stock class handles individual positional data including the ticker, number of shares
cost to enter the position, settlement date, sector etc. Called by Portfolio class 
during instantiation and updates. Can be accessed to retrieve positional data.
Additionally, each Stock objects carries with it its own historical price data in the
form of a pandas dataframe. The class currently pulls data from yahoo finance using the
yfinance API.

TODO:
    - Finish to string method for printing
    - organize historical data
'''

# Importing Libraries
import numpy as np
import pandas as pd
import yfinance as yf

'''
Stock()
Param:
    ticker <string> -- string of stock symbol as traded i.e Apple -> 'APPL'
    amnt <int> -- number of shares purchased or sold
    cost <float> -- cost of purchase or sale (amnt * price)
    sd <datetime> -- settlement date of purchase
    date <datetime> -- date (? not sure what for)
    sector <string> -- sector of company i.e Apple -> 'TECH'
'''
class Stock():
    def __init__(self, ticker, amnt, cost, sd, date, sector):
        self.ticker = ticker
        self.amnt = int(amnt)
        self.cost = float(cost)
        self.sd = sd
        self.sector = sector
        self.yfTicker = yf.Ticker(self.ticker)
        self.history = self.yfTicker.history(start=sd, end=date)
        self.currentPrice = self.history['Close'].tail(1).to_list()


    # return ticker <string>
    def getTicker(self):
        return self.ticker

    # return amnt <int> (number of shares held)
    def getAmnt(self):
        return self.amnt

    # return cost <float> (cost at purchase)
    def getCost(self):
        return self.cost

    # return settlement date sd <datetime>
    def getSD(self):
        return self.sd

    # return sector <string> (business sector of company)
    def getSector(self):
        return self.sector

    # set amnt to newAmnt <int> (buying/selling shares)
    def setAmnt(self, newAmnt):
        self.amnt = newAmnt
        return self.amnt

    # set cost to newCost <float> (buying/selling shares)
    def setCost(self, newCost):
        self.cost = newCost
        return self.cost

    # set settlement date sd to newSD <datetime> (buying/selling shares)
    def setSD(self, newSD):
        self.sd = newSD
        return self.sd

    #TODO: Finish To string method
    def __str__(self):
        output = "[" + self.ticker + "]:\n\tAmount:\t" + str(self.amnt) + "\n\tCost:\t" + str(self.cost) + "\n\tSD:\t" + self.sd + "\n\tSector\t" + self.sector
        return output
