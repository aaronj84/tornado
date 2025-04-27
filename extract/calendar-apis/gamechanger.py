import requests
from ics import Calendar

# 1. Your Gamechanger calendar link
##danr yankees
url = 'https://api.team-manager.gc.com/ics-calendar-documents/user/416c3290-6f46-485a-9be7-29f68e8cfbf3.ics?teamId=36583f79-f818-4965-a6c6-0f333404bfd5&token=e00cf042f29d76eaf1cb154e510f5a3c02439945d9de4d75f4c5c4e7616dea14'

# 2. Fetch the calendar file
response = requests.get(url)
response.raise_for_status()  # Throws an error if download fails

# 3. Parse the .ics data
calendar = Calendar(response.text)

# 4. Explore the events
for event in calendar.events:
    print(f"Event: {event.name}")
    print(f"Starts: {event.begin}")
    print(f"Ends: {event.end}")
    print(f"Description: {event.description}")
    print(f"Location: {event.location}")
    print("---")
    # print(f"Extra : {event.extra or 'N/A'}")

