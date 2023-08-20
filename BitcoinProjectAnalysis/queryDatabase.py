import pandas as pd
import connectDB.connection as dbCollection

def getCollectionData():
    collection = dbCollection.connectDb()
    
    # Consultar dados do MongoDB e criar um DataFrame com Pandas
    data = list(collection.find())
    df = pd.DataFrame(data)

        # Convertendo as colunas de tempo para o formato datetime
    for col in ['time_period_start', 'time_period_end', 'time_open', 'time_close']:
        df[col] = pd.to_datetime(df[col])

    # Ordenando o DataFrame pela coluna 'time_period_start'
    df.sort_values('time_period_start', inplace=True)

    # Definindo 'time_period_start' como o índice
    df.set_index('time_period_start', inplace=True)        
    
    return df