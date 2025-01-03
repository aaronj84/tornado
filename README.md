
<div align="center"> <br /> 
  
![airflow-postresql-docker](https://github.com/user-attachments/assets/a10113ed-9d2d-4c36-90c2-84798657aa58)


  </a> <br /> 
  <div>
    <img src="https://img.shields.io/badge/-Docker-black?style=for-the-badge&logo=docker&logoColor=white&color=0db7ed" alt="Docker" />
    <img src="https://img.shields.io/badge/-PostgreSQL-blue?style=for-the-badge&logo=postgresql&logoColor=white&color=336791" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/-Python-yellow?style=for-the-badge&logo=python&logoColor=white&color=306998" alt="Python" />
  </div>
  <h1 align="center">🔄 ELT Project with Docker and PostgreSQL ,Airbyte, dbt, and Airflow</h1>
  <h3 align="center">A Custom Extract, Load, Transform (ELT) Process using Docker and PostgreSQL</h3>
  <p align="center">Effortlessly extract data from a source PostgreSQL database, transform it, and load it into a destination database using Docker containers.</p> 
</div>

## 📋 <a name="table">Table of Contents</a>

1. 🤖 [Introduction](#introduction)
2. 🌲 [Branches](#branches)
3. ⚙️ [Tech Stack](#tech-stack)
4. 🔋 [How It Works](#how-it-works)
5. 🤸 [Getting Started](#getting-started)
6. 🔗 [Links](#links)
7. 🚀 [Conclusion](#conclusion)

## <a name="introduction">🤖 Introduction</a>

This ELT project demonstrates a custom Extract, Load, Transform (ELT) process that uses Docker and PostgreSQL. The project includes a source database, a destination database, and an ELT script that facilitates the data transfer. The key components are:

- Extracts data from a source PostgreSQL database.
- Transforms data as necessary using a Python script.
- Loads the transformed data into a destination PostgreSQL database.
- All processes are orchestrated using Docker.

## <a name="branches">🌲 Branches</a>

This project has multiple branches to explore different ELT workflows. Switch to the appropriate branch to try out other implementations:

| Branch    | Description                                                                                     | Switch Command                                                                 |
|-----------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `main`    | ELT Project with Docker and PostgreSQL (current branch).                                        | `git checkout main`                                                           |
| `airbyte` | A Dockerized ELT Workflow Using PostgreSQL, dbt, and Airflow.                                   | `git checkout airbyte`                                                        |
| `airflow` | ELT Project with Docker, PostgreSQL, dbt, and Airflow.                                          | `git checkout airflow`                                                        |
| `cron`    | ELT Project with Docker, PostgreSQL, dbt, and CRON.                                             | `git checkout cron`                                                           |
| `dbt`     | ELT Project with Docker, PostgreSQL, and dbt.                                                   | `git checkout dbt`                                                            |

To switch branches, run the appropriate `git checkout` command listed above.

## <a name="tech-stack">⚙️ Tech Stack</a>

- **Docker**: Containerization of the entire application stack.
- **PostgreSQL**: Both source and destination databases for data storage.
- **Python**: ELT scripting language for extracting, transforming, and loading data.
- **Docker Compose**: Manages multi-container Docker applications.

## <a name="how-it-works">🔋 How It Works</a>

#### Docker Compose
- The `docker-compose.yaml` file orchestrates three Docker containers:
  1. **Source PostgreSQL Database**: Contains sample data.
  2. **Destination PostgreSQL Database**: Where the data is loaded.
  3. **ELT Python Script**: The Python script that extracts data from the source, transforms it, and loads it into the destination database.

#### ELT Process
- The Python script (`elt_script.py`) waits for the source PostgreSQL database to become available.
- Once available, the script uses `pg_dump` to extract the data.
- It then uses `psql` to load the extracted data into the destination PostgreSQL database.

#### Database Initialization
- The `init.sql` script initializes the source database with sample data, including tables for users, films, categories, actors, and film actors.

## <a name="getting-started">🤸 Getting Started</a>

Follow these steps to set up and run the project locally.

**Prerequisites**:
Make sure you have Docker and Docker Compose installed on your machine.

**Clone the Repository**:
Clone the repository to your local machine:
```bash
git clone https://github.com/TheODDYSEY/Elt-Project.git
```

**Navigate to the Directory**:
Navigate to the project directory:
```bash
cd Elt-Project
```

**Start Docker Containers**:
Run the following command to start the Docker containers:
```bash
docker-compose up
```

**Access the Destination Database**:
Once the containers are up and running, the ELT process will start automatically. After the ELT process completes, you can access the source and destination PostgreSQL databases on ports `5433` and `5434`, respectively. Use the following command to access the destination PostgreSQL database:
```bash
docker exec -it elt-project-destination_postgres-1 psql -U postgres
```

**View the Database and Tables**:
```bash 
\c destination_db   -- Connects to the destination database named destination_db
\dt                 -- Lists all tables in the current database
```

## <a name="branches">🌲 Branches</a>

This project has multiple branches to explore different ELT workflows. Switch to the appropriate branch to try out other implementations:

| Branch    | Description                                                                                     | Switch Command                                                                 |
|-----------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `main`    | ELT Project with Docker and PostgreSQL (current branch).                                        | `git checkout main`                                                           |
| `airbyte` | A Dockerized ELT Workflow Using PostgreSQL, dbt, and Airflow.                                   | `git checkout airbyte`                                                        |
| `airflow` | ELT Project with Docker, PostgreSQL, dbt, and Airflow.                                          | `git checkout airflow`                                                        |
| `cron`    | ELT Project with Docker, PostgreSQL, dbt, and CRON.                                             | `git checkout cron`                                                           |
| `dbt`     | ELT Project with Docker, PostgreSQL, and dbt.                                                   | `git checkout dbt`                                                            |

To switch branches, run the appropriate `git checkout` command listed above.

## <a name="links">🔗 Links</a>

- [GitHub Repository](https://github.com/TheODDYSEY/Elt-Project)

## <a name="conclusion">🚀 Conclusion</a>

Congratulations! You’ve successfully set up and run the ELT project using Docker and PostgreSQL. Explore the other branches to experience more advanced ELT workflows and expand your understanding of modern data processing pipelines.
