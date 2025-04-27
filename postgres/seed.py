import psycopg2
from config import DB_CONFIG

# Connect to your Postgres instance
conn = psycopg2.connect(**DB_CONFIG)

cur = conn.cursor()

schemes = {'stg','app','config'}

for schema in schemes:
    cur.execute(f"CREATE SCHEMA IF NOT EXISTS {schema};")

conn.commit()

# DROP TABLES first if re-running
cur.execute("""
DROP TABLE IF EXISTS stg.events, app.fact_event_participation, app.dim_event, app.dim_roles, app.dim_person, config.calendar CASCADE;
""")

# Create tables
cur.execute("""
CREATE TABLE stg.events (
    event_title VARCHAR(255),
    team_name VARCHAR(255),
    location_name VARCHAR(255),
    location_address VARCHAR(255),
    event_start_dts TIMESTAMP,
    event_end_dts TIMESTAMP,
    uniform VARCHAR(255)
);
""")

# Create tables
cur.execute("""
CREATE TABLE app.dim_event (
    event_id SERIAL PRIMARY KEY,
    event_title VARCHAR(255),
    team_name VARCHAR(255),
    location_name VARCHAR(255),
    location_address VARCHAR(255),
    event_start_dts TIMESTAMP,
    event_end_dts TIMESTAMP,
    uniform VARCHAR(255)
);
""")

cur.execute("""
CREATE TABLE app.dim_roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(100) -- Examples: Player, Driver, Spectator, Home Babysitter, Stay Home
);
""")

cur.execute("""
CREATE TABLE app.dim_person (
    person_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    can_drive BOOLEAN,
    can_supervise BOOLEAN
    -- Preference (future state) can be added later
);
""")

cur.execute("""
CREATE TABLE config.calendar (
    calendar_id SERIAL PRIMARY KEY,
    calendar_name VARCHAR(255),
    url TEXT,
    calendar_type VARCHAR(50),
    auth TEXT
);
""")

cur.execute("""
CREATE TABLE app.fact_event_participation (
    id SERIAL PRIMARY KEY,
    event_id INT REFERENCES app.dim_event(event_id),
    role_id INT REFERENCES app.dim_roles(role_id),
    person_id INT REFERENCES app.dim_person(person_id),
    depart_from_event_id INT, -- Could later be a FK to dim_event(event_id)
    depart_time TIMESTAMP,
    depart_from_address VARCHAR(255),
    drive_duration INTERVAL,
    arrival_time TIMESTAMP,
    field VARCHAR(255)
);
""")

conn.commit()

print("Tables created successfully!")

# Optional: Insert dummy data if you want
cur.execute("""
INSERT INTO app.dim_roles (role_name)
VALUES
('Player'), ('Driver'), ('Spectator'), ('Home Babysitter'), ('Stay Home');
""")

cur.execute("""
INSERT INTO app.dim_person (name, can_drive, can_supervise)
VALUES
('Aaron', TRUE, TRUE),
('Jenn', TRUE, TRUE),
('Fynn', TRUE, TRUE),
('Svea', FALSE, TRUE),
('Svea', FALSE, TRUE),
('Danr', FALSE, FALSE),
('Rudi', FALSE, FALSE),
('Mari', FALSE, FALSE),
('Bryn', FALSE, FALSE);
""")

cur.execute("""
INSERT INTO config.calendar (calendar_name, url, calendar_type, auth)
VALUES
 ('CFC Academy','http://ical-cdn.teamsnap.com/team_schedule/d2bcf3f4-8973-43e0-9f9f-a3425adc97e3.ics','ics','none')
,('Rudi B15 United','http://ical-cdn.teamsnap.com/team_schedule/filter/games/68e18647-9f03-43f2-ac56-342f1c60568b.ics','ics','none')
,('Danr Yankees','https://api.team-manager.gc.com/ics-calendar-documents/user/416c3290-6f46-485a-9be7-29f68e8cfbf3.ics?teamId=36583f79-f818-4965-a6c6-0f333404bfd5&token=e00cf042f29d76eaf1cb154e510f5a3c02439945d9de4d75f4c5c4e7616dea14','ics','none')
,('Svea BHS Golf','http://ical-cdn.teamsnap.com/team_schedule/d2bcf3f4-8973-43e0-9f9f-a3425adc97e3.ics','google','none')
;""")

conn.commit()
print("Sample data inserted!")

cur.close()
conn.close()
