import logging
import sys
from logging import DEBUG, INFO
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("item_service_app")
logger.setLevel(level=INFO)

# Log format handler
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(level=INFO)
console_handler.setFormatter(formatter)

# File handler
file_handler = TimedRotatingFileHandler(
    "app.log",
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8",
    delay=True
)
file_handler.setLevel(level=DEBUG)
file_handler.setFormatter(formatter)

# Attach handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)