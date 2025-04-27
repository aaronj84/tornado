import psycopg2

# Connect to your Postgres instance
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydb",
    user="myuser",
    password="mypassword"
)

cur = conn.cursor()

# DROP TABLES first if re-running
cur.execute("""
DROP TABLE IF EXISTS fact_event_participation, dim_event, dim_roles, dim_person, config_calendar CASCADE;
""")

# Create tables
cur.execute("""
CREATE TABLE dim_event (
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
CREATE TABLE dim_roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(100) -- Examples: Player, Driver, Spectator, Home Babysitter, Stay Home
);
""")

cur.execute("""
CREATE TABLE dim_person (
    person_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    can_drive BOOLEAN,
    can_supervise BOOLEAN
    -- Preference (future state) can be added later
);
""")

cur.execute("""
CREATE TABLE config_calendar (
    calendar_id SERIAL PRIMARY KEY,
    calendar_name VARCHAR(255),
    url TEXT,
    type VARCHAR(50),
    auth TEXT
);
""")

cur.execute("""
CREATE TABLE fact_event_participation (
    id SERIAL PRIMARY KEY,
    event_id INT REFERENCES dim_event(event_id),
    role_id INT REFERENCES dim_roles(role_id),
    person_id INT REFERENCES dim_person(person_id),
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
INSERT INTO dim_roles (role_name)
VALUES
('Player'), ('Driver'), ('Spectator'), ('Home Babysitter'), ('Stay Home');
""")

cur.execute("""
INSERT INTO dim_person (name, can_drive, can_supervise)
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
INSERT INTO config_calendar (calendar_name, url, calendar_type, auth)
VALUES
('CFC Academy','http://ical-cdn.teamsnap.com/team_schedule/d2bcf3f4-8973-43e0-9f9f-a3425adc97e3.ics','ics','none'),
('Rudi B15 United','http://ical-cdn.teamsnap.com/team_schedule/filter/games/68e18647-9f03-43f2-ac56-342f1c60568b.ics','ics','none'),
('Danr Yankees','http://ical-cdn.teamsnap.com/team_schedule/d2bcf3f4-8973-43e0-9f9f-a3425adc97e3.ics','ics','none');
""")

conn.commit()
print("Sample data inserted!")

cur.close()
conn.close()
