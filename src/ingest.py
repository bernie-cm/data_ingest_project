import pandas as pd
import logging
import numpy as np
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def read_csv_log_rows(file_path):
    """Reads a csv file and logs the number of rows."""
    file = Path(file_path)

    if not file.exists():
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"No such file: {file_path}")

    df = pd.read_csv(file)
    logging.info(f"Loaded {len(df):,} rows from {file_path}")
    return df

if __name__ == "__main__":
    df = read_csv_log_rows("data/large_sales.csv")
    print(df.head())

