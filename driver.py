# Driver Code

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
