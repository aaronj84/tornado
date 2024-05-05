docker compose up
docker compose down -v

ELT STEP
docker up
docker compose down -v
docker exec -it elt-project-destination_postgres-1 psql -U postgres

AIRFLOW STEP
$ docker compose up init-airflow -d
docker compose up