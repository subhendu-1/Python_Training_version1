# log.py
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('app.log')
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)

# Avoid duplicate log entries
if not logger.handlers:
    logger.addHandler(file_handler)
