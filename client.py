import os
from dotenv import load_dotenv
from binance.client import Client

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Retrieve the credentials safely from the environment
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = os.getenv("BASE_URL")

# 3. Check to ensure the keys were loaded properly
if not API_KEY or not API_SECRET:
    raise ValueError("Missing Binance API Key or Secret in .env file!")

# 4. Initialize the Binance Client
# By default, python-binance points to production. 
# We configure it to use the Demo/Testnet URL provided in your .env file.
client = Client(api_key=API_KEY, api_secret=API_SECRET)

# Adjust the internal API endpoints if a custom base URL (like demo/testnet) is provided
if BASE_URL:
    client.API_URL = BASE_URL
    # For futures specifically, the python-binance library uses a separate property:
    client.FUTURES_URL = f"{BASE_URL.rstrip('/')}/fapi"

print("Binance Client initialized successfully!")