import logging
import os
from logging.handlers import TimedRotatingFileHandler

# Define the path to save log files
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Log file path
LOG_FILE = os.path.join(LOG_DIR, 'data_collection_service.log')

def setup_logger():
    """
    Sets up a logger with a specific format and rotating file handler.
    """
    # Create a logger object
    logger = logging.getLogger('DataCollectionService')
    logger.setLevel(logging.DEBUG)  # Set the minimum log level

    # Create a file handler that logs messages to a file
    handler = TimedRotatingFileHandler(LOG_FILE, when='midnight', interval=1, backupCount=7)
    handler.setLevel(logging.DEBUG)  # Set the log level for the file handler

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Set the formatter for the handler
    handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(handler)

    # Stream handler to output logs to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Set the log level for the console
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Example usage:
if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Logger is configured and ready to use.")
    logger.debug("This is a debug message.")
    logger.error("This is an error message.")
