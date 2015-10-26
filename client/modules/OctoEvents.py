# -*- coding: utf-8-*-
import random
import re
import json
import httplib
from datetime import datetime
from dateutil import tz
from client import jasperpath

WORDS = ["OCTO", "EVENTS"]

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by telling a joke.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    events = "These are the last 5 Octo Events. "
    JasperKey = "API-get your own key"
    connection = httplib.HTTPConnection("kno2-deploy.cloudapp.net", 80)
    connection.connect()
    connection.request('GET', '/api/events', None, {"X-Octopus-ApiKey": JasperKey})
    result = json.loads(connection.getresponse().read())
    index = 0
    for attribute, value in result.iteritems():
        if attribute == "Items":
            for each_dict in value[:5]:
                friendlydate = datetime.strptime(each_dict.get("Occurred"), "%Y-%m-%dT%H:%M:%S.%f+00:00")
                from_zone = tz.tzutc()
                to_zone = tz.tzlocal()
                friendlydate = friendlydate.replace(tzinfo=from_zone)
                central = friendlydate.astimezone(to_zone)
                events += "Event: " + each_dict.get("Message") + " was performed by " + each_dict.get("Username") + " at " + \
                      central.strftime("%m/%d/%Y at %H:%M Local Time.")

    mic.say(events)



def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bocto events\b', text, re.IGNORECASE))
