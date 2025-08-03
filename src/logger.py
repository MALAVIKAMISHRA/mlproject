import logging
import os
from datetime import datetime

# 1. Define the log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path to the 'logs' directory
logs_path = os.path.join(os.getcwd(), "logs")

# 3. Create the 'logs' directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# 4. Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# 5. --- THIS IS THE FIX ---
# Get the root logger and remove any existing handlers
# This ensures basicConfig will work and configure the logger from scratch.
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
# -------------------------


# 6. Setup new logging configuration to use the correct file path
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

