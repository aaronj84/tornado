## ELT Project with Docker and PostgreSQL

Welcome to the ELT project repository! This project demonstrates a custom Extract, Load, Transform (ELT) process using Docker and PostgreSQL. Below, you'll find details on the repository structure, how it works, and instructions to get started.

### Repository Structure

- **docker-compose.yaml**: This file orchestrates Docker containers for the project. It defines services for the source PostgreSQL database, destination PostgreSQL database, and the ELT script.
  
- **elt_script**: Contains the ELT script and Dockerfile for the ELT service.
  - **Dockerfile**: Sets up a Python environment and installs the PostgreSQL client. It also copies the ELT script into the container.
  - **elt_script.py**: Performs the ELT process, waiting for the source PostgreSQL database to become available, dumping its data to a SQL file, and loading it into the destination PostgreSQL database.
  
- **source_db_init**: Includes the SQL script for initializing the source database with sample data.
  - **init.sql**: Initializes tables for users, films, film categories, actors, and film actors, and inserts sample data.

### How It Works

#### Docker Compose
- Using the `docker-compose.yaml` file, three Docker containers are spun up:
  1. Source PostgreSQL database with sample data.
  2. Destination PostgreSQL database.
  3. Python environment to run the ELT script.

#### ELT Process
- The `elt_script.py` waits for the source PostgreSQL database to become available.
- Once available, the script uses `pg_dump` to dump the source database to a SQL file.
- It then uses `psql` to load this SQL file into the destination PostgreSQL database.

#### Database Initialization
- The `init.sql` script initializes the source database with sample data by creating tables and populating them.

### Getting Started

To get started with the ELT project, follow these steps:

1. **Prerequisites**: Ensure you have Docker and Docker Compose installed on your machine.

2. **Clone the Repository**: Clone the repository to your local machine:
   ```bash
   git clone https://github.com/TheODDYSEY/Elt-Project.git
   ```

3. **Navigate to the Directory**: Navigate to the project directory:
   ```bash
   cd Elt-Project
   ```

4. **Start Docker Containers**: Run the following command to start the Docker containers:
   ```bash
   docker-compose up
   ```

5. **Access the Destination Database**: Once all containers are up and running, the ELT process will start automatically. After the ELT process completes, you can access the source and destination PostgreSQL databases on ports 5433 and 5434, respectively. Use the following command to access the destination PostgreSQL database:
   ```bash
   docker exec -it elt-project-destination_postgres-1 psql -U postgres
   ```

### Conclusion

Congratulations! You've successfully set up and run the ELT project using Docker and PostgreSQL.