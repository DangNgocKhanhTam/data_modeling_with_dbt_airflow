
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 9),
    'retries': 1
}

with DAG(
    dag_id='dbt_bigquery',
    default_args=default_args,
    schedule_interval='@daily',  
    catchup=False
) as dag:
    
    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='dbt run --profiles-dir /opt/airflow/de_project'
    )

    run_dbt