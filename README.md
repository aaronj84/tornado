
<div align="center"> 
  <a href="https://github.com/your-username/elt-project" target="_blank">
    <img src="./assets/images/elt-project-banner.png" alt="Project Banner" /> 
  </a> 
  <br />
  <div>
    <img src="https://img.shields.io/badge/-Docker-blue?style=for-the-badge&logo=docker&logoColor=white&color=2496ED" alt="Docker" />
    <img src="https://img.shields.io/badge/-PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white&color=316192" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/-dbt-orange?style=for-the-badge&logo=dbt&logoColor=white&color=FF694B" alt="dbt" />
    <img src="https://img.shields.io/badge/-Airflow-blue?style=for-the-badge&logo=apache-airflow&logoColor=white&color=017CEE" alt="Airflow" />
  </div>
  <h1 align="center">⚙️ ELT Project</h1>
  <h3 align="center">A Dockerized ELT Workflow Using PostgreSQL, dbt, and Airflow</h3>
  <p align="center">Automate your data extraction, loading, and transformation processes with this scalable and modular setup.</p>
</div>

---

## 📋 <a name="table">Table of Contents</a>

1. 🤖 [Introduction](#introduction)  
2. ⚙️ [Tech Stack](#tech-stack)  
3. 🔋 [Features](#features)  
4. 🤸 [Quick Start](#quick-start)  
5. 🛠️ [Repository Structure](#repository-structure)  
6. 🕸️ [How It Works](#how-it-works)  
7. 🔗 [Connecting and Accessing Services](#connecting-and-accessing-services)  
8. 🚀 [Conclusion](#conclusion)

---

## <a name="introduction">🤖 Introduction</a>

The ELT Project demonstrates a comprehensive workflow for extracting, loading, and transforming data using modern tools like Docker, PostgreSQL, dbt, and Airflow. 

This project includes:

- A source PostgreSQL database initialized with sample data.
- An automated ELT process using a Python script to migrate data between databases.
- dbt models for data transformation and analytics.
- Airflow orchestration for seamless workflow automation and monitoring.

---

## <a name="tech-stack">⚙️ Tech Stack</a>

- **Docker**: For containerizing and orchestrating services.  
- **PostgreSQL**: Relational database for source and destination data storage.  
- **dbt**: Data transformation and analytics.  
- **Apache Airflow**: Workflow orchestration and scheduling.  
- **Python**: ELT script implementation.  

---

## <a name="features">🔋 Features</a>

👉 **Fully Dockerized Environment:** Easily spin up isolated services using Docker Compose.  
👉 **Automated ELT Process:** A Python script automates data extraction, loading, and transformation between databases.  
👉 **Data Transformation with dbt:** Use dbt models for efficient SQL-based data transformations.  
👉 **Workflow Orchestration with Airflow:** Schedule and monitor ELT tasks using Airflow's web-based UI.  
👉 **Sample Data Initialization:** Source PostgreSQL database is preloaded with user-friendly sample data.  
👉 **Dynamic Data Migration:** Transfer data seamlessly between source and destination databases.  

---

## <a name="quick-start">🤸 Quick Start</a>

Follow these steps to set up and run the project locally:

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/elt-project.git
   cd elt-project
   ```

2. Start the services using Docker Compose:  
   ```bash
   docker-compose up
   ```

3. To stop services and clean up resources:  
   ```bash
   docker-compose down -v
   ```

---

## <a name="repository-structure">🛠️ Repository Structure</a>

- **`docker-compose.yaml`**: Configures services for the project.  
- **`elt_script`**: Contains the Python ELT script and Dockerfile.  
  - **`elt_script.py`**: Automates the ELT process between databases.  
  - **`Dockerfile`**: Builds the Python environment.  
- **`source_db_init`**: SQL script to initialize the source database with sample data.  
- **`airflow`**: DAGs and dependencies for workflow orchestration.  
  - **`dags`**: Contains the Airflow DAG definition file.  

---

## <a name="how-it-works">🕸️ How It Works</a>

1. **Dockerized Services**  
   - Containers include the source and destination PostgreSQL databases, Python ELT service, dbt, and Airflow.

2. **ELT Process**  
   - The ELT script extracts data from the source database, loads it into the destination database, and ensures smooth data transfer.

3. **Data Transformation**  
   - dbt applies SQL models to transform and analyze the loaded data.

4. **Orchestration**  
   - Airflow schedules and monitors the entire process via a web-based UI.

---

## <a name="connecting-and-accessing-services">🔗 Connecting and Accessing Services</a>

### PostgreSQL
To connect to the destination database:  
```bash
docker exec -it elt-project-destination_postgres-1 psql -U postgres
```

Once connected:  
```sql
\c destination_db   -- Switch to the destination database  
\dt                 -- List tables  
```

### Airflow  
Access the Airflow web UI at: [http://localhost:8080](http://localhost:8080)  
- **Username:** airflow  
- **Password:** password  

---

## <a name="conclusion">🚀 Conclusion</a>

This project equips you with the tools to manage ELT workflows effectively. Whether you’re migrating data, transforming it for analytics, or scheduling workflows, this modular setup has you covered. Happy coding! 🚀

