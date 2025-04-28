#this file is to test out the functionality of the app, which involves analyzing the upcoming events and asking chatgpt to help me plan the day
#for version 0.0 (Apr 27), i'm not going to work on refinements of quality with the chatgpt responses, i'll just take what it gives me and go with it

def get_people_events_dict(daysAheadInt,personName=""):
    people = []

    if personName:
        people.append(personName)
    else:
        print("look up all the people names from the people table")

    for person in people:
        print(f"Find all the events for {person} {daysAheadInt} days from now.")
    
    return {}

def who_has_what_where_when(daysAheadInt):
    print(f"I'll tell you by person what activities are happeneing {daysAheadInt} from now")
    
    response = "Nobody has nothing"
    return response

def who_drives_whom_where_when(daysAheadInt):
    print(f"I'll tell you who needs to drive whom wohin")
    response = "UberTeen for everyone suckaz"
    return response

if __name__ == "__main__":
    byPerson = who_has_what_where_when(0)
    print(byPerson)

    byDriver = who_drives_whom_where_when(0)
    print(byDriver)

    perPerson = get_people_events_dict("Fynn")
    print(perPerson)