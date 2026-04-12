import os
from datetime import datetime

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Default data file
DEFAULT_DATA_PATH = os.path.join(DATA_DIR, "cleaned_cpi_data.csv")

# Category mapping for file names
CATEGORIES = {
    "Food": "Food",
    "Transport": "Transport",
    "Clothing And Footwear": "Clothing_And_Footwear",
    "Health": "Health",
    "Housing Water Electricity Gas And Other Fuel": "Housing_Water_Electricity_Gas_And_Other_Fuel"
}

# Last known CPI indices (update these with your actual latest values from NBS)
LAST_KNOWN_CPI = {
    "Food": 783.0,
    "Transport": 552.81,
    "Clothing And Footwear": 512.54,
    "Health": 474.83,
    "Housing Water Electricity Gas And Other Fuel": 519.65
}