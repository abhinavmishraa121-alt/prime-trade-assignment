import os
import logging

def setup_logging():
    """
    Configure logging to display logs on the console and save them to a file.
    """
    # 1. 'logs' naam ka folder check karein, agar nahi hai toh create karein
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
        
    log_filepath = os.path.join(log_directory, "bot.log")

    # 2. Log message ka standard format define karein
    # Format: [YYYY-MM-DD HH:MM:SS] [LEVEL] [FILENAME:LINE] Message
    log_format = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 3. Root logger create karein aur uska base level INFO set karein
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Purane handlers ko clear karein taaki duplicate logs na aayein
    if logger.hasHandlers():
        logger.handlers.clear()

    # 4. File Handler (Log file mein write karne ke liye)
    file_handler = logging.FileHandler(log_filepath, encoding='utf-8')
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    # 5. Console Handler (Terminal par print karne ke liye)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    logging.info("Logging successfully configured. Logs will be saved to logs/bot.log")

# Is function ko setup_logging call karke initialize kar dein jab is file ko import kiya jaye
setup_logging()