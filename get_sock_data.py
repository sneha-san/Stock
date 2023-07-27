import pandas as pd
import yfinance as yf
from bsedata.bse import BSE
from NSEDownload import stocks


def get_ticker(country):
    if country == 'India':
        df = pd.read_csv('data/nse_stocks.csv')
        return df['SYMBOL'].tolist()
    elif country == 'USA':
        df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
        return df

def get_scripcode(tickerSymbol):
    df = pd.read_csv('data/indian_stock.csv')
    return df[df['Security Id'] == tickerSymbol]['Security Code'].tolist()[0]
def get_indian_stock(tickerSymbol,startDate,endDate):
    # scripcode = get_scripcode(tickerSymbol)
    print(str(startDate),endDate,tickerSymbol)
    df = stocks.get_data(stock_symbol=tickerSymbol, start_date=str(startDate), end_date=str(endDate))
    return df


def get_history(tickerSymbol, periodd):
    scripcode =get_scripcode(tickerSymbol)
    print(type(str(scripcode)))
    b = BSE()
    his = dict(b.getPeriodTrend(str(scripcode), periodd))
    print(his)
    return his

def get_usa_stock(tickerSymbol,start_date,end_date):
    tickerData = yf.download(tickerSymbol, period='1d', start=start_date, end=end_date)  # Get ticker data
    tickerData2 = yf.Ticker(tickerSymbol)
    return tickerData,tickerData2
