import pandas as pd
import yfinance as yf

def get_ticker(country):
    if country == 'India':
        df = pd.read_csv('data/indian_stock.csv')
        return df['Security Id'].tolist()
    elif country == 'USA':
        df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
        return df

def get_indian_stock(ticker,startDate,endDate):
    pass

def get_usa_stock(tickerSymbol,start_date,end_date):
    tickerData = yf.download(tickerSymbol, period='1d', start=start_date, end=end_date)  # Get ticker data
    tickerData2 = yf.Ticker(tickerSymbol)
    return tickerData,tickerData2
