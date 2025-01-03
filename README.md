
<div align="center"> <br /> 
  <a href="https://youtu.be/zgGhzuBZOQg" target="_blank">
    <img src="./public/assets/images/tickethub.png" alt="Project Banner" /> 
  </a> <br /> 
  <div>
    <img src="https://img.shields.io/badge/-Docker-blue?style=for-the-badge&logo=docker&logoColor=white&color=2496ED" alt="Docker" /> 
    <img src="https://img.shields.io/badge/-PostgreSQL-blue?style=for-the-badge&logo=postgresql&logoColor=white&color=336791" alt="PostgreSQL" /> 
    <img src="https://img.shields.io/badge/-dbt-black?style=for-the-badge&logo=dbt&logoColor=white&color=2D3748" alt="dbt" />
    <img src="https://img.shields.io/badge/-CRON-green?style=for-the-badge&logo=linux&logoColor=white&color=2E8B57" alt="CRON" />
  </div>
  <h1 align="center">🔄 ELT Project with Docker, PostgreSQL, dbt, and CRON</h1>
  <h3 align="center">A Custom Extract, Load, Transform (ELT) Process with Docker, PostgreSQL, dbt, and CRON Automation</h3>
  <p align="center">A seamless solution for automating data extraction, loading, and transformation with regular updates via CRON jobs.</p> 
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

This project demonstrates a custom Extract, Load, Transform (ELT) process using Docker, PostgreSQL, dbt (data build tool), and CRON for automation. The project facilitates data migration, transformation, and regular updates to ensure the destination database reflects the most current data from the source.

- **Docker** orchestrates the containerized services for easy deployment.
- **PostgreSQL** is used as the source and destination database.
- **dbt** handles data transformations and analysis.
- **CRON** automates the ELT process by scheduling regular updates.

## <a name="tech-stack">⚙️ Tech Stack</a>

- Docker
- PostgreSQL
- dbt (Data Build Tool)
- Python (for the ELT script)
- Docker Compose (for container orchestration)
- CRON (for task scheduling and automation)

## <a name="features">🔋 Features</a>

👉 **Docker Orchestration:** All components, including PostgreSQL and dbt, are managed via Docker Compose, allowing for easy replication and environment setup.

👉 **ELT Script:** A custom ELT process is implemented, extracting data from the source PostgreSQL database and loading it into the destination PostgreSQL database. The script uses `pg_dump` to dump the data and `psql` to load it.

👉 **Data Transformation with dbt:** Once data is loaded, dbt transforms it using predefined models and SQL queries.

👉 **CRON Job Automation:** A CRON job automates the ELT process by running the ELT script at specified intervals (currently set for every day at 3 AM). The CRON job ensures that the data in the destination database is regularly updated with the latest data from the source database.

## <a name="quick-start">🤸 Quick Start</a>

Follow these steps to set up the project locally on your machine.

**Prerequisites**

Make sure you have the following installed on your machine:

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

This will start the source and destination PostgreSQL databases, along with a Python environment for the ELT script, and schedule the CRON job.

**Running the ELT Process**

The ELT process will start automatically once the containers are up and running. The CRON job ensures that the ELT script is executed every day at 3 AM, updating the destination database with the latest data from the source database.

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
    # Code to execute ELT process
    ...

run_elt_script()  # Execute ELT script
```

### CRON Job Setup: `Dockerfile` (in the `elt_script` folder)

```Dockerfile
# Dockerfile for ELT service with CRON job

# Set up the Python environment and PostgreSQL client
FROM python:3.9-slim

# Install required packages
RUN apt-get update && apt-get install -y cron postgresql-client

# Copy ELT script into the container
COPY elt_script.py /app/elt_script.py

# Set up CRON job to run ELT script every day at 3 AM
RUN echo "0 3 * * * python /app/elt_script.py" >> /etc/cron.d/elt-cron
RUN chmod 0644 /etc/cron.d/elt-cron

# Start the cron service
CMD cron && tail -f /var/log/cron.log
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
- [CRON Job Documentation](https://en.wikipedia.org/wiki/Cron)

## <a name="more">🚀 Conclusion</a>

Congratulations! You've successfully set up the ELT project using Docker, PostgreSQL, dbt, and CRON automation. The CRON job ensures that the data is regularly updated, making this a powerful tool for automating data workflows. Feel free to explore the code, make modifications, and experiment with the CRON job schedule.

If you have any questions or encounter any issues, refer to the documentation or reach out for assistance. Happy coding!
