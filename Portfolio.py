# Portfolio.py
# Handles CSV importing and handling

#Library Import:
import pandas as pd

def main():
    filePath = input("* Please enter file path for portfolio data: ")
    print("* Loading data from file...")
    rawPortfolio = pd.read_csv(filePath, skiprows=1)
    rawPortfolio.columns = ['Ticker',
                            'SettlementDate',
                            'Principal']
    print(rawPortfolio)

if __name__ == '__main__':
    main()
