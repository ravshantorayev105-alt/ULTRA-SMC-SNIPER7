import requests
import pandas as pd

def get_data(symbol, tf, key):

    url=f"https://api.twelvedata.com/time_series?symbol={symbol}&interval={tf}&apikey={key}&outputsize=100"

    r=requests.get(url).json()

    df=pd.DataFrame(r["values"])

    df=df.astype(float)

    df=df.iloc[::-1]

    return df
