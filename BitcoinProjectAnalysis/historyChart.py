import pandas as pd
import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
import mplfinance as mpf
# from pymongo import MongoClient
import queryDatabase as data

# # Conectar ao MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['bitcoin']
# collection = db['bitcoinCollection']

# # Consultar dados do MongoDB e criar um DataFrame com Pandas
# data = list(collection.find())
# df = pd.DataFrame(data)
def createHistoryGraph():
    bitcoinData = data.getCollectionData()

    # Convertendo as colunas de tempo para o formato datetime
    for col in ['time_period_start', 'time_period_end', 'time_open', 'time_close']:
        bitcoinData[col] = pd.to_datetime(bitcoinData[col])
  
    # Ordenando o DataFrame pela coluna 'time_period_start'
    bitcoinData.sort_values('time_period_start', inplace=True)

    # Definindo 'time_period_start' como o índice
    bitcoinData.set_index('time_period_start', inplace=True)

    # Criando o gráfico dos últimos 5 anos
    plt.figure(figsize=(10,5))
    plt.plot(bitcoinData['price_close'].last('5Y'))
    plt.title('Preço de fechamento nos últimos 5 anos')
    plt.xlabel('Data')
    plt.ylabel('Preço de fechamento (USD $)')
    plt.show(block=False)