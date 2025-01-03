
<div align="center"> <br /> 

  <h1 align="center">🔄 ELT Project with Docker, PostgreSQL, and dbt</h1>
  <h3 align="center">A Custom Extract, Load, Transform (ELT) Process with Docker and dbt Integration</h3>
  <p align="center">A streamlined process to manage and transform data using Docker, PostgreSQL, and dbt for improved data analysis and management.</p> 
  
  <div>
    <img src="https://img.shields.io/badge/-Docker-blue?style=for-the-badge&logo=docker&logoColor=white&color=2496ED" alt="Docker" /> 
    <img src="https://img.shields.io/badge/-PostgreSQL-blue?style=for-the-badge&logo=postgresql&logoColor=white&color=336791" alt="PostgreSQL" /> 
    <img src="https://img.shields.io/badge/-dbt-black?style=for-the-badge&logo=dbt&logoColor=white&color=2D3748" alt="dbt" />
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

This project demonstrates a custom Extract, Load, Transform (ELT) process using Docker, PostgreSQL, and dbt (data build tool). It allows for efficient data migration and transformation in a seamless, containerized environment. Here's an overview of the project:

- **Docker** manages containerization, allowing for easy replication and environment setup.
- **PostgreSQL** serves as both the source and destination databases.
- **dbt** runs data transformation tasks, helping to convert raw data into valuable insights.

## <a name="tech-stack">⚙️ Tech Stack</a>

- Docker
- PostgreSQL
- dbt (Data Build Tool)
- Python (for the ELT script)
- Docker Compose (for container orchestration)

## <a name="features">🔋 Features</a>

👉 **Docker Orchestration:** All services are managed through Docker Compose, allowing for quick deployment and management of containers for PostgreSQL and dbt.

👉 **ELT Script:** The project includes a custom ELT process that extracts data from a source PostgreSQL database, loads it into a destination database, and then transforms the data using dbt.

👉 **Database Initialization:** The `init.sql` script initializes a sample source database with user, film, and actor data.

👉 **Data Transformation with dbt:** After loading the data into the destination database, dbt is used to run transformation tasks on the data.

👉 **PostgreSQL Database Management:** Both source and destination PostgreSQL databases are set up in Docker containers for easy access and management.

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

This will start the source and destination PostgreSQL databases, along with a Python environment to run the ELT script.

**Running the ELT Process**

Once the containers are up and running, the ELT process will begin automatically. After the process completes, dbt will run transformation tasks.

**Accessing the Databases**

You can access the source and destination PostgreSQL databases on ports `5433` and `5434`, respectively.

```bash
docker exec -it elt-project-destination_postgres-1 psql -U postgres
```

To connect to the destination database:

```bash
\c destination_db   -- Connect to the destination database
\dt                 -- List all tables in the current database
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

## <a name="more">🚀 Conclusion</a>

You've successfully set up and run the ELT project using Docker, PostgreSQL, and dbt. Feel free to explore the code and experiment further with the ELT process and dbt integration. If you have any questions or encounter any issues, please refer to the documentation or reach out to the project maintainers for assistance. Happy coding!
