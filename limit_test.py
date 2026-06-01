from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    order = client.futures_create_order(
        symbol="BTCUSDT",
        side="SELL",
        type="LIMIT",
        quantity=0.001,
        price="100000",
        timeInForce="GTC"
    )

    print("SUCCESS")
    print(order)

except Exception as e:
    print("ERROR")
    print(e)