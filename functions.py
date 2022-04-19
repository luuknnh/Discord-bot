import requests, yaml, os
import json
from dotenv import load_dotenv

load_dotenv()
zen = os.getenv('ZENQUOTES')
queuetimestov = os.getenv('QUEUETIMESTOVERLAND')
queuetimesefteling = os.getenv('QUEUETIMESEFTELING')
bored = os.getenv('BOREDAPI')


def get_quote():
    response = requests.get(zen)
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "  - " + json_data[0]['a']
    return quote


def get_wachttijd_efteling_anderrijk():

    response = requests.get(queuetimesefteling)
    formated_response = response.json()
    x = formated_response['lands']
    
    for i in x:
        if i['name'] == 'Anderrijk':
            
            return yaml.dump(i, allow_unicode=True)

def get_wachttijd_efteling_bosrijk():

    response = requests.get(queuetimesefteling)
    formated_response = response.json()
    x = formated_response['lands']

    for i in x:
        if i['name'] == 'Efteling Village Bosrijk':
            return yaml.dump(i, allow_unicode=True)

def get_wachttijd_efteling_fantasierijk():

    response = requests.get(queuetimesefteling)
    formated_response = response.json()
    x = formated_response['lands']

    for i in x:
        if i['name'] == 'Fantasierijk':
            return yaml.dump(i, allow_unicode=True)
        
def get_wachttijd_efteling_marerijk():

    response = requests.get(queuetimesefteling)
    formated_response = response.json()
    x = formated_response['lands']

    for i in x:
        if i['name'] == 'Marerijk':
            return yaml.dump(i, allow_unicode=True)

def get_wachttijd_efteling_reizenrijk():

    response = requests.get(queuetimesefteling)
    formated_response = response.json()
    x = formated_response['lands']

    for i in x:
        if i['name'] == 'Reizenrijk':
            return yaml.dump(i, allow_unicode=True)
        
def get_wachttijd_efteling_ruigrijk():

    response = requests.get(queuetimesefteling)
    formated_response = response.json()
    x = formated_response['lands']

    for i in x:
        if i['name'] == 'Ruigrijk':
            return yaml.dump(i, allow_unicode=True)

def get_action():
    response = requests.get(bored)
    formated_response = response.json()
    activity = formated_response['activity']
    return activity
  