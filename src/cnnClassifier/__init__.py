import os
import sys
import logging

# Define the logging format 
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


# Define the directory and file path for the log files
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")

# Create the log directory if it doesn't exist 
os.makedirs(log_dir, exist_ok=True)

# Configure for logging settings
logging.basicConfig(
    level= logging.INFO, # Set the logging level to info
    format= logging_str, # Set the logging format

    handlers=[
        logging.FileHandler(log_filepath), # Log to file 
        logging.StreamHandler(sys.stdout) # Log to console
    ]
)

# Create a logger object 
logger = logging.getLogger("cnnClassifierLogger")