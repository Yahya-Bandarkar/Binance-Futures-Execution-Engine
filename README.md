# Binance Futures Execution Engine

A Python CLI application for executing Market and Limit orders on Binance Futures Testnet (USDT-M).

## ✨ Features

* 📈 Market Orders
* 🎯 Limit Orders
* 🔄 BUY and SELL Support
* 💻 CLI-based Input
* ✅ Input Validation
* 📝 Logging
* ⚠️ Error Handling
* 💰 Profit & Loss (P&L) Tracking
* 📊 Portfolio Summary Dashboard
* 📜 Order History Tracking
* 🔔 Price Alerts & Notifications
* 📈 Real-Time Price Simulation


## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

## Project Structure

```text
bot/
├── client.py
├── orders.py
├── validators.py
└── logging_config.py

cli.py
requirements.txt
trading.log
```

## Logging

API requests and responses are stored in `trading.log`.

## Bonus Implemented

Enhanced CLI UX with formatted output, improved validation messages, clear success/failure notifications, and user-friendly command examples.

## Author

Yahya Bandarkar
