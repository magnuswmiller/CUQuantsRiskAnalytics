# Portfolio.py
# Handles CSV importing and handling

#Library Import:
import pandas as pd
import numpy as np

class Stock():
    def __init__(self, ticker, amnt, cost, sd, sector):
        self.ticker = ticker
        self.amnt = int(amnt)
        self.cost = float(cost)
        self.sd = sd
        self.sector = sector

    def getTicker(self):
        return self.ticker

    def getAmnt(self):
        return self.amnt

    def getCost(self):
        return self.cost

    def getSD(self):
        return self.sd

    def getSector(self):
        return self.sector

    def setAmnt(self, newAmnt):
        self.amnt += newAmnt
        return self.amnt

    def setCost(self, newCost, isBuy):
        if isBuy:
            self.cost += newCost
        else:
            self.cost -= newCost
        return self.cost

    def setSD(self, newSD):
        self.sd = newSD
        return self.sd

    #TODO: Finish To string method
    def __str__(self):
        output = "[" + self.ticker + "]:\n\tAmount:\t" + str(self.amnt) + "\n\tCost:\t" + str(self.cost) + "\n\tSD:\t" + self.sd + "\n\tSector\t" + self.sector
        return output

#TODO: Finish portfolio class and link with stocks
class Portfolio():
    def __init__(self, log={}, positions=[], cash=0.0, sd=0.0, pnl=0.0, beta=0.0, treynor=0.0,
                 sharpe=0.0, jensens=0.0, stddev=0.0, var=0.0, cvar=0.0):
        self.log = log
        self.positions = positions
        self.cash = cash
        self.sd = sd
        self.pnl = pnl
        self.beta = beta
        self.treynor = treynor
        self.sharpe = sharpe
        self.jensens = jensens
        self.stddev = stddev
        self.var = var
        self.cvar = cvar

    def inLog(self, key):
        return (key in self.log.keys())

    def getPositions(self):
        return self.positions
    
    def getLenth(self):
        return len(self.positions)

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

    def addPosition(self, key, value, stock):
        self.log.update({key: value})
        self.positions.append(stock)

        return -1

    def updatePosition(self, ticker, amnt, cost, sd):
        return -1

    #TODO
    def exitPosition(self, target):
        return -1

    #TODO: Finish to string method
    def __str__(self):
        print("-- Open Portfolio Positions --")
        for i in range(len(self.positions)):
            print(self.positions[i])
        return "-- End of Portfolio --"

def portfolioParse(rawPortfolioArr, portfolio):
    for i in range(len(rawPortfolioArr)):
        ticker = rawPortfolioArr[i][0]
        amnt = rawPortfolioArr[i][1]
        costPS = rawPortfolioArr[i][2]
        sd = rawPortfolioArr[i][3]
        sector = rawPortfolioArr[i][4]
        if not(portfolio.inLog(ticker)):
            info = rawPortfolioArr[i][1:]
            portfolio.addPosition(ticker, amnt, Stock(ticker, amnt, costPS*amnt, sd, sector))
        else:
            portfolio.updatePosition(ticker, amnt, costPS, sd)
    return -1 

def main():
    filePath = input("* Please enter file path for portfolio data: ")
    print("* Loading data from file...")
    rawPortfolio = pd.read_csv(filePath, skiprows=1)
    rawPortfolio.columns = ['Ticker',
                            'Quantity',
                            'Cost PS',
                            'DOA',
                            'Action',
                            'Sector']
    print(rawPortfolio)
    rawPortfolioArr = np.asarray(rawPortfolio)
    currentPortfolio = Portfolio()
    portfolioParse(rawPortfolioArr, currentPortfolio)
    print(currentPortfolio)

if __name__ == '__main__':
    main()

'''
filePath = input("* Please enter file path for portfolio data: ")
rawPortfolio = pd.read_csv(filePath, skiprows=1)
rawPortfolio.columns = ['Ticker',
                        'Quantity',
                        'Price',
                        'DOA',
                        'Action',
                        'Sector']
rawPortfolioArr = np.asarray(rawPortfolio)
currentPortfolio = Portfolio(portfolioParse(rawPortfolioArr))
aapl_stock = currentPortfolio.findStockByTicker("AAPL")
print(aapl_stock)
'''
