import logging
from pathlib import Path

# Ensure logs folder exists
Path("logs").mkdir(exist_ok=True)

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/rtgs.log"),
        logging.StreamHandler()  # also show in terminal
    ]
)

logger = logging.getLogger("rtgs")
