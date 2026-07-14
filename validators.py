import logging

# Hum isme wahi logger use karenge jo humne logging_config mein setup kiya hai
logger = logging.getLogger(__name__)

def validate_symbol(symbol: str) -> str:
    """
    Validate and format the trading symbol (e.g., converts 'btc-usdt' or 'btcusdt' to 'BTCUSDT').
    """
    if not symbol or not isinstance(symbol, str):
        logger.error("Symbol validation failed: Symbol must be a non-empty string.")
        raise ValueError("Symbol must be a non-empty string.")
    
    # Remove extra spaces, convert to uppercase, and remove dashes/underscores
    clean_symbol = symbol.strip().upper().replace("-", "").replace("_", "")
    
    # Basic check: Binance symbols usually end with USDT, BUSD, etc., and are at least 5 chars
    if len(clean_symbol) < 5:
        logger.error(f"Symbol validation failed: '{clean_symbol}' is too short.")
        raise ValueError(f"'{clean_symbol}' does not look like a valid Binance symbol.")
        
    return clean_symbol


def validate_side(side: str) -> str:
    """
    Validate if the order side is either BUY or SELL.
    """
    if not side or not isinstance(side, str):
        logger.error("Side validation failed: Side must be a string.")
        raise ValueError("Side must be a string.")
        
    clean_side = side.strip().upper()
    if clean_side not in ["BUY", "SELL"]:
        logger.error(f"Side validation failed: '{clean_side}'. Must be 'BUY' or 'SELL'.")
        raise ValueError("Side must be either 'BUY' or 'SELL'.")
        
    return clean_side


def validate_leverage(leverage: int) -> int:
    """
    Validate if the leverage is within the allowed futures range (typically 1x to 125x).
    """
    try:
        lev = int(leverage)
    except (ValueError, TypeError):
        logger.error(f"Leverage validation failed: '{leverage}' is not a valid number.")
        raise ValueError("Leverage must be a valid integer.")
        
    if lev < 1 or lev > 125:
        logger.error(f"Leverage validation failed: {lev}x. Must be between 1 and 125.")
        raise ValueError("Leverage must be between 1 and 125.")
        
    return lev