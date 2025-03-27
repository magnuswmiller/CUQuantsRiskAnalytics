# portfolio object class
'''
Portfolio.py outlines the portfolio class. This file houses the portfolio
objects used by the driver. Each instantiation uses 'stock' objects during
initialization. Each stock object carries with itself its own stock history.
Getter and Setter functions used to retrieve and set local variables to the 
portfolio object. Can be used when writing calculations.

TODO:
    - finish writing position_exit() function to better calculate trades.
    - finish writing to string method for driver output
    - finish integrating with portfolio parser class
    - Finish developing calculations.
        - Current value
        - cash on hand
        - PnL 
        - sd
        - beta
        - sharpe
        - var
        - cvar
        - treynor
        - jensens
        - etc.
        - start with all time before implementing with capabilities for varying
        time frames/windows: 1d,5d,2w,1m,2m,3m,6m,1yr,2yr,5yr,all
          time, ytd
'''


#TODO: Finish portfolio class and link with stocks
import numpy as np
import pandas as pd

class Portfolio():
    '''
    Portfolio()
    Param:
        - date <string> -- current date in 'yyyy-mm-dd' format
        - cash <float> -- current cash on hand provided by user
        - log <dict> -- dictionary of all positions (ticker:amnt of shares)
        - positions <list> -- list of all positions <Stock>
        - local variables <float> -- variables for calculation values, default to 0.0 until fully dev-
          eloped later.
    Return:
        - -1 <int> -- successful creation of Portfolio object
    '''
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

    # return boolean T/F if 'key" is in dictionary of all positions
    def inLog(self, key):
        return (key in self.log.keys())

    # return list of all positions (list of <Stock> objects
    def getPositions(self):
        return self.positions

    # return the cash value <float>
    def getCash(self):
        return self.cash
    
    # return the number of positions in portfolio <int>
    def getLength(self):
        return len(self.positions)

    # return the date of the last trade <date.time>
    def getSD(self):
        return self.sd
    
    # return the PnL value <float> in dollars
    def getPnL(self):
        return self.pnl

    # return the beta value of portfolio <float>
    def getBeta(self):
        return self.beta

    # return the Treynor value of portfolio <float>
    def getTreynor(self):
        return self.treynor

    # return the Sharpe ratio of the portfolio <float>
    def getSharpe(self):
        return self.sharpe

    # return the Jensens value of the portfolio <float>
    def getJensens(self):
        return self.jensens

    # return the standard deviation of the portfolio <float>
    def getStdDev(self):
        return self.stddev

    # return the Value at Risk of the portfolio <float>
    def getVaR(self):
        return self.var
    
    # return the Conditional Value at Risk of the Portfolio <float>
    def getCVaR(self):
        return self.cvar

    # add position with ticker 'key' and number of shares 'value' as <Stock> stock
    def addPosition(self, key, value, stock):
        self.log.update({key: value})
        self.positions.append(stock)
        self.cash -= stock.getCost()
        return -1

    # update the position with ticker 'ticker', number of shares 'amnt', cost 'cost'
    # settlement date 'sd', and buy/sell type 'isBuy' <bool>
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
    # exit position by removing it from portfolio and accounting for profit/loss
    # in conversion to cash
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
    # returns portfolio as string in printable format
    def __str__(self):
        print("-- Open Portfolio Positions --")
        for i in range(len(self.positions)):
            print(self.positions[i])
        return "-- End of Portfolio --"
