from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Hebert',
    'start_date': datetime(2024, 8, 26)
}

