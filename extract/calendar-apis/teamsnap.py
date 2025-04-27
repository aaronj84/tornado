import requests
from ics import Calendar

# 1. Your TeamSnap calendar link
##"CFC" Mari Bryn Cal##url = 'http://ical-cdn.teamsnap.com/team_schedule/d2bcf3f4-8973-43e0-9f9f-a3425adc97e3.ics'
url = 'http://ical-cdn.teamsnap.com/team_schedule/filter/games/68e18647-9f03-43f2-ac56-342f1c60568b.ics'##Rudi B15 AJ


# 2. Fetch the calendar file
response = requests.get(url)
response.raise_for_status()  # Throws an error if download fails

# 3. Parse the .ics data
calendar = Calendar(response.text)

# 4. Explore the events
for event in calendar.events:
    print(event.uid)
    print(f"Event: {event.name}")
    print(f"Starts: {event.begin}")
    print(f"Ends: {event.end}")
    print(f"Description: {event.description}")
    print(f"Location: {event.location}")
    print("---")

