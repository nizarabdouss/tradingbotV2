import pandas as pd 
import datetime

f = open('Binance_BTCUSDT_1h.csv', 'r')

#print(f.read())

d = {'Date':[],
    'High':[],
    'Low':[],
    'Open':[],
    'Close':[],
    'Volume':[],
    'Adj_Close':[]}

next(f)
f = f.readlines()[1:]

for i in f:
    filter = i.strip().split(',')
    if len(filter) > 1:
        d['Date'].append(filter[1][:10])
        d['High'].append(filter[4])
        d['Low'].append(filter[5])
        d['Open'].append(filter[3])
        d['Close'].append(filter[6])
        d['Volume'].append(filter[8])
        d['Adj_Close'].append(filter[6])

df = pd.DataFrame(data = d)

print(df)
#print(d)

def get_data_in_range(startDate: datetime, endDate: datetime):
    pass

