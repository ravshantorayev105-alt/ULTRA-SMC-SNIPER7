def liquidity(df):

    if df.low.iloc[-1] < df.low.iloc[-2]:
        return "BUY"

    if df.high.iloc[-1] > df.high.iloc[-2]:
        return "SELL"

    return None
