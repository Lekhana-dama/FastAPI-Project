import logging
from logging.handlers import RotatingFileHandler

file_handler=RotatingFileHandler(
    "app.log",
    maxBytes=5*1024*1024,
    backupCount=4
)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        file_handler
    ]
)
