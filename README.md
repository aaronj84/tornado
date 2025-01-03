
<div align="center"> <br /> 

  </a> <br /> 

  <h1 align="center">🔄 ELT Project with Docker, PostgreSQL, dbt, and Airflow</h1>
  <h3 align="center">A Comprehensive Extract, Load, Transform (ELT) Process with Docker, PostgreSQL, dbt, and Airflow for Workflow Automation</h3>
  <p align="center">A powerful solution for automating data extraction, transformation, and loading with streamlined orchestration using Airflow.</p> 
    <div>
    <img src="https://img.shields.io/badge/-Docker-blue?style=for-the-badge&logo=docker&logoColor=white&color=2496ED" alt="Docker" /> 
    <img src="https://img.shields.io/badge/-PostgreSQL-blue?style=for-the-badge&logo=postgresql&logoColor=white&color=336791" alt="PostgreSQL" /> 
    <img src="https://img.shields.io/badge/-dbt-black?style=for-the-badge&logo=dbt&logoColor=white&color=2D3748" alt="dbt" />
    <img src="https://img.shields.io/badge/-Airflow-lightgrey?style=for-the-badge&logo=apache-airflow&logoColor=white&color=0179B5" alt="Airflow" />
  </div>
</div>

## 📋 <a name="table">Table of Contents</a>

1. 🤖 [Introduction](#introduction)
2. ⚙️ [Tech Stack](#tech-stack)
3. 🔋 [Features](#features)
4. 🤸 [Quick Start](#quick-start)
5. 📝 [Code Snippets](#snippets)
6. 🔗 [Links](#links)
7. 🚀 [Conclusion](#more)

## <a name="introduction">🤖 Introduction</a>

This project demonstrates a robust Extract, Load, Transform (ELT) process using Docker, PostgreSQL, dbt (data build tool), and Apache Airflow for workflow orchestration. The project provides a powerful pipeline that automates the extraction of data from a source PostgreSQL database, loads it into a destination PostgreSQL database, and transforms the data using dbt. Airflow is used to orchestrate the entire process, ensuring automated and scheduled workflows.

- **Docker** orchestrates all components, enabling easy deployment and isolation of services.
- **PostgreSQL** is used as the source and destination database.
- **dbt** is responsible for transforming the data according to predefined models.
- **Airflow** automates and schedules tasks for the ELT process, allowing for robust workflow management and monitoring.

## <a name="tech-stack">⚙️ Tech Stack</a>

- Docker
- PostgreSQL
- dbt (Data Build Tool)
- Apache Airflow
- Python (for ELT script)
- Docker Compose (for orchestration)

## <a name="features">🔋 Features</a>

👉 **Docker Orchestration:** The project leverages Docker Compose to manage multiple containers for PostgreSQL (source and destination), dbt, Python (for the ELT process), and Airflow.

👉 **ELT Script:** A custom ELT process that extracts data from the source database using `pg_dump` and loads it into the destination database with `psql`.

👉 **Data Transformation with dbt:** dbt is used to run SQL transformations on the loaded data to structure it according to defined models.

👉 **Airflow Workflow Orchestration:** Apache Airflow schedules and manages the execution of the ELT process and dbt tasks. With Airflow, tasks are orchestrated in a workflow and can be monitored and controlled through a web UI.

## <a name="quick-start">🤸 Quick Start</a>

Follow these steps to set up the project locally on your machine.

**Prerequisites**

Make sure you have the following installed:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

**Cloning the Repository**

```bash
git clone https://github.com/your-username/elt-project.git
cd elt-project
```

**Installation**

Build and run the Docker containers using Docker Compose:

```bash
docker-compose up
```

This command will spin up the following containers:

- Source PostgreSQL database with sample data.
- Destination PostgreSQL database.
- Python environment for running the ELT script.
- dbt for data transformation.
- Airflow for workflow orchestration.

**Running the ELT Process**

Airflow will automatically trigger the ELT process at the scheduled time as defined in the DAG (`elt_and_dbt.py`). This will:
- Dump data from the source PostgreSQL database.
- Load it into the destination PostgreSQL database.
- Trigger dbt transformations.

**Stopping and Removing Containers**

To stop the containers and remove volumes, run:

```bash
docker-compose down -v
```

## <a name="snippets">📝 Code Snippets</a>

### ELT Script: `elt_script.py`

```python
# ELT Script: elt_script.py

def run_elt_script():
    # Code to execute the ELT process: dumping from source DB and loading into destination DB
    ...

run_elt_script()  # Execute ELT process
```

### Airflow DAG: `elt_and_dbt.py` (in the `airflow/dags` folder)

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def run_elt():
    # Code to call the ELT script (elt_script.py)
    ...

def run_dbt():
    # Code to run dbt transformations
    ...

# Airflow DAG Definition
dag = DAG(
    'elt_and_dbt',
    description='Orchestrates the ELT and dbt workflows',
    schedule_interval=timedelta(days=1),  # Runs daily
    start_date=datetime(2025, 1, 3),
    catchup=False,
)

elt_task = PythonOperator(
    task_id='run_elt',
    python_callable=run_elt,
    dag=dag,
)

dbt_task = PythonOperator(
    task_id='run_dbt',
    python_callable=run_dbt,
    dag=dag,
)

# Task Dependencies
elt_task >> dbt_task  # Run dbt after ELT completes
```

### Airflow Dockerfile (for setting up Airflow environment)

```Dockerfile
# Dockerfile for Airflow

FROM apache/airflow:2.3.0

# Install any additional dependencies
RUN pip install apache-airflow-providers-postgres

# Set up Airflow environment and entrypoint
USER root
COPY dags/ /opt/airflow/dags/

CMD ["airflow", "scheduler"]
```

### Database Initialization: `init.sql`

```sql
-- Initialize Source Database
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO users (username, email) VALUES
('john_doe', 'john@example.com'),
('jane_doe', 'jane@example.com');
```

## <a name="links">🔗 Links</a>

- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [dbt Documentation](https://docs.getdbt.com/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)

## <a name="more">🚀 Conclusion</a>

Congratulations! You've successfully set up the ELT project with Docker, PostgreSQL, dbt, and Airflow. The integration of Airflow allows for automated, scheduled execution and monitoring of your ELT processes. Feel free to explore the code, adjust the DAG schedule, and experiment with the workflows.

If you have any questions or encounter issues, please refer to the documentation or reach out for support. Happy coding!

