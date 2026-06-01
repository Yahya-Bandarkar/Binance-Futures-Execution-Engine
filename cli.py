import argparse
import logging

from bot.orders import place_order
from bot.validators import validate
import bot.logging_config

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

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
    print("----------------")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price: {args.price}")

    print("\nRESPONSE")
    print("----------------")
    print("Order ID:", response["orderId"])
    print("Status:", response["status"])
    print("Executed Qty:", response["executedQty"])
    print("Average Price:", response.get("avgPrice", "N/A"))

    print("\nSUCCESS: Order submitted successfully")

except Exception as e:

    logging.error(str(e))

    print("\nFAILED")
    print("Error:", e)