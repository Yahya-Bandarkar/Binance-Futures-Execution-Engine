import argparse
import logging

from bot.orders import place_order
from bot.validators import validate
import bot.logging_config

parser = argparse.ArgumentParser(
    description="Binance Futures Execution Engine"
)

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    print("\n" + "=" * 50)
    print(" BINANCE FUTURES EXECUTION ENGINE ")
    print("=" * 50)

    validate(
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    logging.info(
        f"Request: Symbol={args.symbol}, "
        f"Side={args.side}, "
        f"Type={args.type}, "
        f"Quantity={args.quantity}, "
        f"Price={args.price}"
    )

    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    logging.info(f"Response: {response}")

    print("\nORDER SUMMARY")
    print("-" * 50)
    print(f"Symbol      : {args.symbol}")
    print(f"Side        : {args.side}")
    print(f"Type        : {args.type}")
    print(f"Quantity    : {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price       : {args.price}")

    print("\nRESPONSE")
    print("-" * 50)
    print(f"Order ID    : {response['orderId']}")
    print(f"Status      : {response['status']}")
    print(f"Executed Qty: {response['executedQty']}")
    print(f"Avg Price   : {response.get('avgPrice', 'N/A')}")

    print("\nSUCCESS: Order submitted successfully")
    print("=" * 50)

except Exception as e:

    logging.error(str(e))

    print("\n" + "=" * 50)
    print(" ORDER FAILED ")
    print("=" * 50)

    print("Error:", e)

    print("\nValid Examples:\n")

    print(
        "Market Order:\n"
        "python cli.py --symbol BTCUSDT "
        "--side BUY --type MARKET "
        "--quantity 0.001\n"
    )

    print(
        "Limit Order:\n"
        "python cli.py --symbol BTCUSDT "
        "--side SELL --type LIMIT "
        "--quantity 0.001 --price 100000\n"
    )