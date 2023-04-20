import os
from datetime import datetime
import logging

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "logs")

os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="[ %(asctime)s ] file name %(filename)s line number %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


