import queryDatabase as data
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd

def createCandlestickChart():
    bitcoinData = data.getCollectionData()
    
    # Criando o gráfico de candlestick dos últimos 30 dias
    data_last_month = data.last('30D')
    # Definindo os dados OHLC (Open, High, Low, Close)
    ohlc = data_last_month[['time_open', 'price_open', 'price_high', 'price_low', 'price_close']].copy()
    # Ajustando o índice para ser do tipo datetime
    ohlc.index = pd.to_datetime(ohlc['time_open'])
    # Renomeando as colunas
    ohlc.rename(columns={'price_open': 'Open', 
                        'price_high': 'High', 
                        'price_low': 'Low', 
                        'price_close': 'Close'}, inplace=True)
    # Criando o gráfico de candlestick
    mpf.plot(ohlc, type='candle', style='charles', title='Gráfico de Candlestick dos últimos 30 dias', ylabel='Preço (USD $)')
    plt.show(block=False)