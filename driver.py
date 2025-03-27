# Driver Code
'''
File handles driving the risk calculator.
Running driver requirements:
    - file path for portfolio trade csv
    - current date in yyyy-mm-dd format
    - amount of current cash on hand
TODO:
    - compile output to pdf file
        - include major metrics
            - PnL
            - sharpe
            - var
            - cvar
            - etc
    - include handling user request for different metrics
'''

# Importing Libraries
import numpy as np
import pandas as pd
import yfinance as yf
from _portfolio_parse import Portfolio_Parse

def main():
    filePath = input("* Please enter file path for portfolio data: ")
    date = input("* Please enter today's date (yyyy-mm-dd): ")
    cash = float(input("* Please enter today's cash on hand: "))
    csv_parser = Portfolio_Parse(filePath, date, cash)
    rawPortfolioArr, currentPortfolio = csv_parser.csv_reader()
    print("* Printing complete portfolio...")
    print(currentPortfolio)

if __name__ == '__main__':
    main()
