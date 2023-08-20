import matplotlib.pyplot as plt
import queryDatabase as data

def createHistoryGraph():
    dfBitCoin = data.getCollectionData()

    # Criando o gráfico dos últimos 5 anos
    plt.figure(figsize=(10,5))
    plt.plot(dfBitCoin['price_close'].last('5Y'))
    plt.title('Preço de fechamento nos últimos 5 anos')
    plt.xlabel('Data')
    plt.ylabel('Preço de fechamento (USD $)')
    plt.show(block=False)