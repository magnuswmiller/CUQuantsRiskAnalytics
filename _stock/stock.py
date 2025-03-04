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
