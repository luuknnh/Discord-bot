import requests, yaml, os
import json
from dotenv import load_dotenv

load_dotenv()
zen = os.getenv('ZENQUOTES')
queuetimes = os.getenv('QUEUETIMES')
bored = os.getenv('BOREDAPI')


def get_quote():
    response = requests.get(zen)
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "  - " + json_data[0]['a']
    return quote


def get_wachttijd():
    response = requests.get(queuetimes)
    formated_response = response.json()

    for i in formated_response['lands']:
        for x in i['rides']:
            
            list = {
            "Naam": x['name'], 
            "Open": x['is_open'],
            "Waiting Time": x['wait_time'],
            }
            print(list)
            hihi = yaml.dump(list, allow_unicode=True)
            f = open("demofile3.txt", "w") 
            f.write(str(hihi))
            f.close()
    return hihi

def get_action():
    response = requests.get(bored)
    formated_response = response.json()
    activity = formated_response['activity']
    return activity
  