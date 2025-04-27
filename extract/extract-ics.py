import sys
import os
import requests
import psycopg2
import psycopg2.extras

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'postgres'))
sys.path.append(parent_dir)

from config import DB_CONFIG
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ics import Calendar as ICSCalendar
from psycopg2.extras import execute_values

@dataclass_json
@dataclass
class ConfigCalendar:
    calendar_id: int
    calendar_name: str
    url: str
    calendar_type: str
    auth: str

# Connect to your Postgres instance
conn = psycopg2.connect(**DB_CONFIG)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

print("opened a cursor")
print("~~~~~~~~~~~\n")

cur.execute("SELECT calendar_id, calendar_name, url, calendar_type, auth FROM config.calendar WHERE calendar_type = 'ics'")
rows = cur.fetchall()

calendars = [ConfigCalendar.from_dict(row) for row in rows]

event_delete_query = "DELETE FROM stg.events WHERE team_name=%s"

event_insert_query = f"""
INSERT INTO stg.events 
    ( event_title
    , team_name
    , location_name
    , location_address
    , event_start_dts
    , event_end_dts
    )
VALUES %s
"""

for calendar in calendars:
    #connect to and call the url
    if calendar.url:
        cal_name = calendar.calendar_name
        cal_url = calendar.url

        print(f"successful connection - clear the table for {cal_name}")
        cur.execute(event_delete_query,(cal_name,))


        #now hit the URL and insert the events to the staging table
        response = requests.get(cal_url)
        response.raise_for_status()

        ics_cal = ICSCalendar(response.text)
        event_rows = []
        
        for event in ics_cal.events:
            event_rows.append([event.name, cal_name, event.description, event.location, event.begin.datetime, event.end.datetime])
            
        print(f"inserting {len(event_rows)} rows to stg.events for {cal_name}")
        execute_values(cur, event_insert_query, event_rows)
        
        conn.commit()
        print("---\n")




    else:
        print("can't connect to",calendar.calendar_name)
  
cur.close()
conn.close()

print("\n~~~~~~~~~~~")
print("bye byeeeee")
cur.close()

