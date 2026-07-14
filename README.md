# Binance Futures Trading Bot

A simple command-line interface (CLI) trading bot built with Python for placing automated market orders on the Binance Futures Demo/Testnet network.

## Features
- **Input Validation**: Automatically cleans and validates inputs (symbols, leverage, and sides) before sending requests to the API.
- **Leverage Configuration**: Automatically sets the futures account leverage before trade execution.
- **Real-time Logging**: Saves all operations and error reports into `logs/bot.log` and displays them in the terminal.

## Project Structure
- `client.py`: Initializes the connection to the Binance API using environment configurations[cite: 1].
- `logging_config.py`: Standardizes terminal and file logging configurations.
- `validators.py`: Handles validation rules for symbols, trade sides, and leverage ranges.
- `orders.py`: Executes leverage change requests and market orders.
- `cli.py`: The entry-point interactive CLI menu for the user.

## Setup Instructions

1. **Clone or Open the Project Directory**
   Ensure all files are placed in your working folder.

2. **Install Dependencies**
   Run the following command in your terminal:
   ```bash
   pip install -r requirements.txt