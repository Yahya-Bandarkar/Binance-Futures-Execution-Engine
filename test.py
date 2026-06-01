from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

order = client.futures_create_order(
    symbol="BTCUSDT",
    side="BUY",
    type="MARKET",
    quantity=0.001
)

print(order)