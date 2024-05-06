## ELT Project with Docker, PostgreSQL, and dbt

Welcome to the ELT project repository! This project showcases a custom Extract, Load, Transform (ELT) process utilizing Docker, PostgreSQL, and dbt (data build tool). Below, you'll find an overview of the repository structure, details on how it works, and instructions to get started.

### Repository Structure

- **docker-compose.yaml**: This file orchestrates Docker containers for the project, defining services for the source PostgreSQL database, destination PostgreSQL database, ELT script, and dbt tasks.
  
- **elt_script**: Contains the ELT script and Dockerfile for the ELT service.
  - **Dockerfile**: Sets up a Python environment, installs the PostgreSQL client, and copies the ELT script into the container.
  - **elt_script.py**: Executes the ELT process, dumping data from the source PostgreSQL database to a SQL file and loading it into the destination PostgreSQL database.
  
- **source_db_init**: Includes the SQL script for initializing the source database with sample data.
  - **init.sql**: Initializes tables for users, films, film categories, actors, and film actors, populating them with sample data.

- **custom_postgres**: Contains project files and configurations for dbt.

### How It Works

#### Docker Compose
- Using the `docker-compose.yaml` file, Docker spins up three containers:
  1. Source PostgreSQL database with sample data.
  2. Destination PostgreSQL database.
  3. Python environment to run the ELT script.

#### ELT Process with dbt Integration
- The `elt_script.py` waits for the source PostgreSQL database to become available, dumps its data to a SQL file, and loads it into the destination PostgreSQL database.
- After the ELT process completes, dbt runs data build tasks to transform and analyze the data further.

```python
# ELT Script: elt_script.py

def run_elt_script():
    # Code to execute ELT process
    ...

run_elt_script()  # Execute ELT script
```

#### Database Initialization
- The `init.sql` script initializes the source database with sample data by creating tables and populating them.

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

### Getting Started

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Run the following command to start the Docker containers:
   ```bash
   docker-compose up
   ```
5. Once all containers are up and running, the ELT process will start automatically.
6. After the ELT process completes, you can access the source and destination PostgreSQL databases on ports 5433 and 5434, respectively.
    ```bash
    docker exec -it elt-project-destination_postgres-1 psql -U postgres
    ```
7. View the database and tables within 
    ```bash
    \c destination_db   -- Connects to the destination database named destination_db
    \dt                 -- Lists all tables in the current database
    ```
### Conclusion

You've successfully set up and run the ELT project using Docker, PostgreSQL, and dbt. Feel free to explore the code and experiment further with the ELT process and dbt integration. If you have any questions or encounter any issues, please refer to the documentation or reach out to the project maintainers for assistance. Happy coding!