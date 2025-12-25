import os
from pathlib import Path

#project directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

#Data directory
DATA_DIR = PROJECT_DIR/"data"
RAW_DATA_DIR = DATA_DIR/"raw"
PROCESSED_DATA_DIR = DATA_DIR/"processed"

#Postgres 
POSTGRES_URI = os.getenv("POSTGRES_URI",
                         "postgresql://credit_user:credit_pass@127.0.0.1:5432/credit_risk_db")


#MLFlow
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI",
                                (PROJECT_DIR/"mlflow").as_uri())
