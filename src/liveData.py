import asyncio
import pandas as pd
import sqlalchemy
import nest_asyncio
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient
from binance import AsyncClient, BinanceSocketManager
import time
import matplotlib.pyplot as plt

symbol = 'ETHUSDT'

nest_asyncio.apply()


engine = sqlalchemy.create_engine('sqlite:///'+symbol+'stream.db')

async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ts = bm.trade_socket(symbol)
    volume = []
    chart = []
    T = time.process_time()
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            createFrame(res).to_sql(symbol, engine, if_exists='append', index = False)
            print(createFrame(res))
def createFrame(res):
    df = pd.DataFrame([res])
    df = df[['s', 'E', 'p']]
    df.columns = ['Symbol', 'Time', 'Price']
    df.Price = float(df.Price)
    df.Time = pd.to_datetime(df.Time, unit = 'ms')

    return df

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())