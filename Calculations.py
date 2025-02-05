## import Portfolio as port
import yfinance as yf


portfolio = {"MSFT" : 30, "AER" : 45, "NVDA" : 24}

# Link portfolio and amnt to csv
def portfolioValue():
    value = 0
    for i in portfolio:
        ticker = yf.Ticker(i)
        stock = ticker.info
        price = stock['previousClose']
        amnt = portfolio[i]
        value = value + (amnt * price)
    return value

# Link portfolio and amnt
def portfolioBeta():
    Vp = portfolioValue()
    totalBeta = 0
    for i in portfolio:
        ticker = yf.Ticker(i)
        stock = ticker.info
        price = stock['previousClose']
        beta = stock['beta']
        amnt = portfolio[i]
        stockValue = price * amnt
        weight = stockValue/Vp
        totalBeta = totalBeta + (beta * weight)
    return totalBeta

print(portfolioBeta())
