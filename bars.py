import json
import os
import re
from math import sqrt
from urllib.request import urlopen


def load_data(file_path):
    if os.path.isfile(file_path) is False:
        url_json = 'https://apidata.mos.ru/v1/features/1796?api_key=c9d98de8f9a903176268131e2a9821d4'
        response = urlopen(url_json)
        response_json = json.loads(response.read().decode('utf-8'))
        with open(file_path, 'w') as file_save:
            json.dump(response_json, file_save)
        return response_json
    else:
        return json.load(open(file_path))


def get_biggest_bar(features):
    bar = max(features, key=lambda x: x['properties']['Attributes']['SeatsCount'])

    return bar['properties']['Attributes']['Name'] if bar else 'failed'


def get_smallest_bar(features):
    bar = min(features, key=lambda x: x['properties']['Attributes']['SeatsCount'])

    return bar['properties']['Attributes']['Name'] if bar else 'failed'


def get_closest_bar(features):

    longitude = float(input('Enter longitude:'))
    latitude = float(input('Enter latitude:'))

    reg_exp = '^-?[0-9]{1,3}(?:\.[0-9]{1,10})?$'

    if not re.match(reg_exp, str(longitude)) or not re.match(reg_exp, str(longitude)):
        print('entered data is not correct')

    closest_distance = None
    bar = None
    for geometry in features:
        geometry_longitude = geometry['geometry']['coordinates'][0]
        geometry_latitude = geometry['geometry']['coordinates'][1]

        distance = sqrt((geometry_longitude - longitude)**2 + (geometry_latitude - latitude)**2)

        if closest_distance is None or closest_distance > distance:
            bar = geometry
            closest_distance = distance

    return bar['properties']['Attributes']['Name'] if not (bar is None) else 'failed'


if __name__ == '__main__':

    bars_json = load_data('bars.json')
    if bars_json:
        print('самый большой бар: ', get_biggest_bar(bars_json['features']))
        print('самый маленький бар: ', get_smallest_bar(bars_json['features']))
        print('самый близкий бар: ', get_closest_bar(bars_json['features']))
