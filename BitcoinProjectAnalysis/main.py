import historyChart as histChart
import candlestickChart as candChart

def execute():
    print("Criando gráfico com histórico de 5 anos")
    histChart.createHistoryGraph();
    
    print("Finalizado")
    print("Criando gráfico Candlestick com histórico de 30 dias")
    
    candChart.createCandlestickChart();
    
    print("Fim")