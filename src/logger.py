import logging
import os
from datetime import datetime

# Print current working directory
print("CWD:", os.getcwd())

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
print("Expected log directory:", logs_dir)

os.makedirs(logs_dir, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)
print("Full log path:", LOG_FILE_PATH)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



if __name__ == "__main__":
    logger.info("Testing log creation from Cursor.")
    print("✅ Log should be written.")
