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
