from pathlib import Path
from src.exporters.export_sqlite import export_to_sqlite
from src.loaders.load_csv import load_csv
from src.transformers.example_transformer import run_transformations

PATH = Path.cwd()

# Load data
data = load_csv(f"{PATH}/src/data/data_cart_update.csv")

# Transform data
data_transformed = run_transformations(data)

# Export data transformed
export_to_sqlite(data_transformed, "rich_customers")
