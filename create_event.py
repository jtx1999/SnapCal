import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


def creat_event(title, location, date, start_time, end_time=None):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credential-cal.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    if end_time is None:
        end_time = str(int(start_time[:2])+1)+start_time[2:]

    event = {
        'summary': title,
        'location': location,
        'start': {
            'dateTime': date+'T'+start_time+'-04:00',
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': date+'T'+end_time+'-04:00',
            'timeZone': 'America/New_York',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

