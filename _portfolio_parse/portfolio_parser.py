# Parser object class
'''
The portfolio_parser() handles the input from the driver function. Instantiation
of the class takes in a file path, current date, and cash on hand. The filepath
must lead to a csv file of proper format (outlined in README.md file. The parser
then iterates over the file and parses the data creating a raw array of information
(rawPortfolioArr) and passes that to portfolio class to create a virtual portfolio.
Used directly by the driver class and instantiates the portfolio class which
instantiates the stock class. For full file structer and inheritance tree, please
refer to the README.MD file.

TODO:
    - include handling of user inputs for calculation extensions (optional arguments
      for additional calculations)
'''

# importing libraries
import pandas as pd
import numpy as np
from _portfolio_parse._portfolio import Portfolio
from _portfolio_parse._portfolio._stock import Stock

'''
Portfolio_Parse
Params:
    filePath -- <string> to csv file of portfolio trade history
    date -- <string> current date in 'yyyy-mm-dd' format
    cash -- <float> current cash on hand
Return:
    <Portfolio_Parse> (class opbject)
'''
class Portfolio_Parse():
    def __init__(self, filePath, date, cash):
        self.filePath = filePath
        self.date = date
        self.cash = cash

    '''
    portfolioParse()
    Param:
        rawPortfolioArr -- <np.array> of csv data in original format
        portfolio -- <Portfolio> empty portfolio object to be populated
        date -- <string> current date in 'yyyy-mm-dd' format
    Return:
        -1 -- <int> successful parsing, portfolio will be populated
    Handles parsing raw portfolio data and converting into Portfolio
    object format.
    '''
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
    
    '''
    csv_reader()
    Param:
    Return:
        rawPortfolioArr -- <np.array> Array of csv contents
        currentPortfolio -- <Portfolio> Empty portfolio object to be populated by parser fxn
    Handles reading in csv data into np.array format and calling neccessary fxns to convert to
    portfolioObject.
    '''
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
