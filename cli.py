import sys
import logging
import logging_config  # Isse logging setup automatically initialize ho jayega
from orders import set_futures_leverage, place_futures_market_order

logger = logging.getLogger(__name__)

def main():
    print("=========================================")
    print("   WELCOME TO BINANCE FUTURES TRADING BOT ")
    print("=========================================\n")
    
    try:
        # 1. User se inputs lein
        symbol = input("Enter Trading Symbol (e.g., BTCUSDT): ")
        leverage_input = input("Enter Leverage (1 to 125): ")
        side = input("Enter Order Side (BUY or SELL): ")
        quantity_input = input("Enter Quantity to Trade (e.g., 0.001): ")
        
        print("\n--- Processing your request ---")
        
        # Data types convert karein taaki functions me sahi format jaye
        leverage = int(leverage_input)
        quantity = float(quantity_input)
        
        # 2. Pehle Leverage set karein
        set_futures_leverage(symbol=symbol, leverage=leverage)
        
        # 3. Agar leverage successfully set ho jaye, toh market order place karein
        order_receipt = place_futures_market_order(symbol=symbol, side=side, quantity=quantity)
        
        print("\n=========================================")
        print("🎉 SUCCESS: Trade Executed Successfully!")
        print(f"Order ID: {order_receipt.get('orderId')}")
        print(f"Status: {order_receipt.get('status')}")
        print("=========================================")
        
    except ValueError as ve:
        # Inputs ya validation errors ko handle karne ke liye
        logger.error(f"Input Validation Error: {str(ve)}")
        print(f"\n❌ Error: {str(ve)}. Please check your inputs and try again.")
        
    except Exception as e:
        # Baaki kisi bhi unexpected API error ko catch karne ke liye
        logger.error(f"Execution Error: {str(e)}")
        print(f"\n❌ Critical Error: Could not execute trade. Check logs/bot.log for details.")

if __name__ == "__main__":
    main()