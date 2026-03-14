import asyncio
from telegram import Bot

from config import TOKEN, CHAT_ID, API_KEY, PAIRS
from engine import get_data
from strategy import liquidity
from risk import calc

bot = Bot(token=TOKEN)


async def send(text):
    await bot.send_message(chat_id=CHAT_ID, text=text)


async def main():

    while True:

        for pair in PAIRS:

            df = get_data(pair,"5min",API_KEY)

            signal = liquidity(df)

            if signal is None:
                continue

            price = df.close.iloc[-1]

            sl,tp = calc(price)

            text=f"""
ULTRA SMC SNIPER V7

PAIR: {pair}
TYPE: {signal}

ENTRY: {price}
SL: {sl}
TP: {tp}

RR: 1:3
"""

            await send(text)

        await asyncio.sleep(300)


asyncio.run(main())
