import json
import os
import re
from urllib.request import urlopen
from math import sqrt

def load_data(filepath):
    if (os.path.isfile(filepath) == False):
        url_json = 'https://apidata.mos.ru/v1/features/1796?api_key=c9d98de8f9a903176268131e2a9821d4'
        barsjson = urlopen(url_json)
        response = json.loads(barsjson.read().decode('utf-8'))
        with open(filepath, "w") as filesave:
            json.dump(response, filesave)
        return response
    else:
        return json.load(open(filepath))

def get_biggest_bar(data):
    bar = max(data['features'], key = lambda x: x['properties']['Attributes']['SeatsCount'])

    return bar['properties']['Attributes']['Name'] if bar else "failed"

def get_smallest_bar(data):
    bar = min(data['features'], key = lambda x: x['properties']['Attributes']['SeatsCount'])

    return bar['properties']['Attributes']['Name'] if bar else "failed"

def get_closest_bar(data, longitude, latitude):

    reg_exp = '^-?[0-9]{1,3}(?:\.[0-9]{1,10})?$'

    if (not re.match(reg_exp, str(longitude)) or not re.match(reg_exp, str(longitude))):
        print("entered data is not correct")

    closest_distance = None
    bar = None
    for item in data['features']:
        item_longitude = item['geometry']['coordinates'][0]
        item_latitude = item['geometry']['coordinates'][1]

        distance = sqrt((item_longitude - longitude)**2 + (item_latitude - latitude)**2);

        if closest_distance == None or closest_distance > distance:
            bar = item
            closest_distance = distance

    return bar['properties']['Attributes']['Name'] if not (bar is None) else "failed"

if __name__ == '__main__':

    filepath = "bars.json"
    deserializes_json = load_data(filepath)
    if (deserializes_json):

        print ("самый большой бар: ", get_biggest_bar(deserializes_json))
        print ("самый маленький бар: ", get_smallest_bar(deserializes_json))

        longitude = float(input('Enter longitude:'))
        latitude = float(input('Enter latitude:'))
        print("самый близкий бар: ", get_closest_bar(deserializes_json, longitude, latitude))
