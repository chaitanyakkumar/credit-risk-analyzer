import sys
sys.path.append("/opt/airflow/project")

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.data.ingest import ingest_raw_tables


default_args = {
    "name" : "ML",
    "depend_on_past" : False,
    "retries" : 1,
}

def run_ingestion():
    from src.data.ingest import ingest_raw_tables
    ingest_raw_tables()

with DAG(dag_id="credit_risk_data_ingestion",
         description="Ingests the raw data into PostgresSQL",
         default_args= default_args,
         start_date=datetime(2024,1,1),
         catchup=False,
         schedule_interval = None,
         tags = ["credit-loan", "raw", "ingestion"]
         ) as dag:
    
    ingest_raw_data_dag = PythonOperator(task_id = "ingest_raw_tables",
                                         python_callable = run_ingestion)
    
    ingest_raw_data_dag

