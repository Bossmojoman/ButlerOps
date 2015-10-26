# -*- coding: utf-8-*-
import random
import re
from client import jasperpath

WORDS = ["FREEDOM", "EAGLE"]

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by telling a joke.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    mic.say("Kaw Kaw")

   

def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bfreedom eagle\b', text, re.IGNORECASE))
