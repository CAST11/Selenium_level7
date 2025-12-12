import logging
import os

def custom_logger(logLevel=logging.DEBUG):

    # Create reports/logs folder if not exists
    log_path = os.path.join("reports", "logs")
    os.makedirs(log_path, exist_ok=True)

    # Log file path
    log_file = os.path.join(log_path, "automation.log")

    # Create logger
#    logger = logging.getLogger(__name__)
    logger = logging.getLogger("selenium_automation")

    logger.setLevel(logLevel)

    # Avoid duplicates
    if not logger.handlers:

        # File handler → write to reports/logs/automation.log
        fileHandler = logging.FileHandler(log_file)
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fileHandler.setFormatter(formatter)

        # Stream handler (console)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.addHandler(streamHandler)

    return logger
