# Portfolio.py
# Handles CSV importing and handling

#Library Import:
import pandas as pd
import numpy as np
import yfinance as yf

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
        self.amnt = newAmnt
        return self.amnt

    def setCost(self, newCost):
        self.cost = newCost
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
    def __init__(self, date, cash=0.0, log={}, positions=[], sd=0.0, pnl=0.0, beta=0.0, treynor=0.0,
                 sharpe=0.0, jensens=0.0, stddev=0.0, var=0.0, cvar=0.0):
        self.date = date
        self.cash = cash
        self.log = log
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

    def inLog(self, key):
        return (key in self.log.keys())

    def getPositions(self):
        return self.positions

    def getCash(self):
        return self.cash
    
    def getLength(self):
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
        self.cash -= stock.getCost()
        return -1

    def updatePosition(self, ticker, amnt, cost, sd, isBuy):
        oldAmnt = self.log.get(ticker)
        oldCost = -1
        index = -1
        for i in range(len(self.positions)):
            if(self.positions[i].getTicker() == ticker):
                index = i
                oldCost = self.positions[i].getCost()
                break
        if isBuy:
            self.log.update({ticker: oldAmnt + amnt})
            self.positions[index].setAmnt(oldAmnt + amnt)
            self.positions[index].setCost(oldCost + cost)
            self.positions[index].setSD(sd)
            self.cash -= amnt
        else:
            if(oldAmnt - amnt) <= 0:
                self.exitPosition(ticker)
            else:
                self.log.update({ticker: oldAmnt - amnt})
                self.positions[index].setAmnt(oldAmnt - amnt)
                self.positions[index].setCost(oldCost - cost)
                self.positions[index].setSD(sd)
                self.cash += amnt
        return -1

    #TODO
    def exitPosition(self, ticker):
        self.log.pop(ticker)
        oldCost = -1
        index = -1
        for i in range(len(self.positions)):
            if(self.positions[i].getTicker() == ticker):
                index = i
                oldCost = self.positions[i].getCost()
                break
        self.cash += oldCost
        self.positions.pop(index)
        return -1

    #TODO: Finish to string method
    def __str__(self):
        print("-- Open Portfolio Positions --")
        for i in range(len(self.positions)):
            print(self.positions[i])
        return "-- End of Portfolio --"

def portfolioParse(rawPortfolioArr, portfolio, date):
    for i in range(len(rawPortfolioArr)):
        ticker = rawPortfolioArr[i][0]
        amnt = rawPortfolioArr[i][1]
        costPS = rawPortfolioArr[i][2]
        sd = rawPortfolioArr[i][3]
        sector = rawPortfolioArr[i][5]
        isBuy = -1
        if(rawPortfolioArr[i][4] == 'BUY'):
            isBuy = True
        else:
            isBuy = False
        if not(portfolio.inLog(ticker)):
            info = rawPortfolioArr[i][1:]
            print("** Adding position to portfolio...")
            portfolio.addPosition(ticker, amnt, Stock(ticker, amnt, costPS*amnt, sd, date, sector))
        else:
            print("** Updating position in portfolio...")
            portfolio.updatePosition(ticker, amnt, costPS, sd, isBuy)
    return -1 

def main():
    filePath = input("* Please enter file path for portfolio data: ")
    date = input("* Please enter today's date (yyyy-mm-dd): ")
    cash = float(input("* Please enter today's cash on hand: "))
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
    currentPortfolio = Portfolio(date, cash)
    print("* Parsing data...")
    portfolioParse(rawPortfolioArr, currentPortfolio, date)
    print("* Data parsing complete.")
    print("* Printing complete portfolio...")
    print(currentPortfolio)

if __name__ == '__main__':
    main()
