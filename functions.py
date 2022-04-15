import requests, yaml
import json

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "  - " + json_data[0]['a']
    return quote


def get_wachttijd():
    response = requests.get("https://queue-times.com/nl/parks/160/queue_times.json")
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
        
  