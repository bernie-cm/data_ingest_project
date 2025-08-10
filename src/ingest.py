import pandas as pd
import logging
import numpy as np

# TODO write a function that reads a CSV and log the row count

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def read_csv_log_rows(filename):
    logger.info(f"Preparing to read {filename}...")
    df = pd.read_csv(filename)
    logger.info(f"Processed and read {len(df)} rows.")

    return df

# Testing
    

