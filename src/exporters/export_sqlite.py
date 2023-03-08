import sqlite3
from pathlib import Path

import pandas as pd

PATH = Path.cwd()


def export_to_sqlite(df: pd.DataFrame, table_name: str):
    conn = sqlite3.connect(f"{PATH}/src/data/cool_customers.db")
    df.to_sql(table_name, conn, if_exists="replace")
    conn.close()
