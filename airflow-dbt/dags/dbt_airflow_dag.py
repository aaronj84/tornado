from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 19),
    'catchup': False
}

dag = DAG(
    'dbt_run_dag',
    default_args=default_args,
    schedule_interval='@daily',  # Runs once per day
    catchup=False
)

# dbt_run = BashOperator(
#     task_id='dbt_run',
#     bash_command='/home/airflow/.local/bin/dbt run',
#     dag=dag
# )

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='/home/airflow/.local/bin/dbt run',
    env={'PATH': '/home/airflow/.local/bin:$PATH'},
    dag=dag
)
