# Portfolio.py
# Handles CSV importing and handling

#Library Import:
import pandas as pd
import numpy as np

class Stock():
    def __init__(self, ticker, amnt, price, sd, sector):
        self.amnt = amnt
        self.price = price
        self.sd = sd
        self.sector = sector

    def getTicker(self):
        return self.ticker

    def getAmnt(self):
        return self.amnt

    def getPrice(self):
        return self.price

    def getSD(self):
        return self.sd

    def getSector(self):
        return self.sector

    def setAmnt(self, newAmnt):
        self.amnt += newAmnt
        return self.amnt

    def setPrice(self, newPrice):
        self.price += newPrice
        return self.price

    def setSD(self.sd, newSD):
        self.sd = newSD
        return self.sd

    #TODO: Finish To string method
    def __str__():
        print()

#TODO: Finish portfolio class and link with stocks
class Portfolio():
    def __init__(self, positions, sd, pnl, beta, treynor, sharpe, jensens, stddev,
                 var, cvar):
        self.positions = positions
        self.sd = sd
        self.pnl = pnl
        self.beta = beta
        self.treynor = treynor
        self.sharpe = sharpe
        self.jensens = jensens
        self.stddev = stddev
        self.var = var
        self.cvar = cvar

    def getPositions(self):
        return self.positions

    def getSD(self):
        return self.sd
    
    def getPnL(self):
        return self.pnl

    def getBeta(self):
        return self.beta

    def getTreynor(self):
        return self.treynor

    def getSharpe(self):
        return self.sharpe

    def getJensens(self):
        return self.jensens

    def getStdDev(self):
        return self.stddev

    def getVaR(self):
        return self.var
    
    def getCVaR(self):
        return self.cvar

    #TODO: finish add
    def addPosition(self, newStock):
        return -1

    #TODO
    def editPosition(self, target):
        return -1

    #TODO
    def exitPosition(self, target):
        return -1

    #TODO: Finish to string method
    def __str__():
        print()

def portfolioParse(rawPortfolioArr):
    positions = {}
    for i in range(len(rawPortfolioArr)):
        if not(rawPortfolioArr[i][0] in positions.keys()):
            info = rawPortfolioArr[i][1:]
            positions.update({rawPortfolioArr[i][0]: info})
    return positions 

def main():
    filePath = input("* Please enter file path for portfolio data: ")
    print("* Loading data from file...")
    rawPortfolio = pd.read_csv(filePath, skiprows=1)
    rawPortfolio.columns = ['Ticker',
                            'Quantity',
                            'Price',
                            'DOA',
                            'Action',
                            'Sector']
    print(rawPortfolio)
    rawPortfolioArr = np.asarray(rawPortfolio)
    currentPortfolio = portfolioParse(rawPortfolioArr)
    print(currentPortfolio)
    print(len(currentPortfolio))

if __name__ == '__main__':
    main()
