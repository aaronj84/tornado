import sys
import os
import psycopg2
import psycopg2.extras

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'postgres'))
sys.path.append(parent_dir)

from config import DB_CONFIG
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Calendar:
    calendar_id: int
    calendar_name: str
    url: str
    calendar_type: str
    auth: str

# Connect to your Postgres instance
conn = psycopg2.connect(**DB_CONFIG)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

print("opened a cursor")
print("~~~~~~~~~~~\n\n\n")

cur.execute("SELECT calendar_id, calendar_name, url, calendar_type, auth FROM config.calendar WHERE calendar_type = 'ics'")
rows = cur.fetchall()

calendars = [Calendar.from_dict(row) for row in rows]

for calendar in calendars:
    #connect to and call the url
    print("Load events from",calendar.calendar_name,"to stg.events")

    


print("\n\n\n~~~~~~~~~~~")
print("bye byeeeee")
cur.close()

