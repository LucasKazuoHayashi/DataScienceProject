import connectDB.connection as dbCollection

def getCollectionData():
    dbCollection.connectDb();
    
    # Consultar dados do MongoDB e criar um DataFrame com Pandas
    data = list(dbCollection.find())
    df = dbCollection.pd.DataFrame(data)
    
    return df