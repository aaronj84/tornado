FROM apache/airflow:latest

USER root
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install dbt-postgres


