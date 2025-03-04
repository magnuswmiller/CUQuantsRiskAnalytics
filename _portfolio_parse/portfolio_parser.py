class Portfolio_Parse():
    def __init__(self, filePath, date, cash):
        self.filePath = filePath
        self.date = date
        self.cash = cash

    def portfolioParse(self, rawPortfolioArr, portfolio, date):
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
    
    def csv_reader(self):
        print("* Loading data from file...")
        rawPortfolio = pd.read_csv(self.filePath, skiprows=1)
        rawPortfolio.columns = ['Ticker',
                                'Quantity',
                                'Cost PS',
                                'DOA',
                                'Action',
                                'Sector']
        print(rawPortfolio)
        rawPortfolioArr = np.asarray(rawPortfolio)
        currentPortfolio = Portfolio(self.date, self.cash)
        print("* Parsing data...")
        self.portfolioParse(rawPortfolioArr, currentPortfolio, self.date)
        print("* Data parsing complete.")
        return rawPortfolioArr, currentPortfolio
