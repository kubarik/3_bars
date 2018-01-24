import json
import re
import sys
from math import sqrt


def load_data(file_path):
    try:
        with open(file_path, 'r') as file_handler:
            return json.load(file_handler)
    except OSError:
        return False


def get_biggest_bar(bars):
    return max(bars,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def distance(bar, coordinates):
    bar_longitude = bar['geometry']['coordinates'][0]
    bar_latitude = bar['geometry']['coordinates'][1]

    return sqrt((bar_longitude - coordinates[0])**2 +
                (bar_latitude - coordinates[1])**2)


def get_closest_bar(bars, coordinates):
    return min(bars, key=lambda bar: distance(bar, coordinates))


def get_gps_coordinates(label):
    reg_exp = '^-?[0-9]{1,3}(?:\.[0-9]{1,10})?$'
    coordinate = input(label)
    if not re.match(reg_exp, coordinate):
        return False

    return float(coordinate)


def output_bar_name(label, bar):
    print(label, bar['properties']['Attributes']['Name'] if bar else 'failed')


if __name__ == '__main__':

    if len(sys.argv) < 2:
        sys.exit('Не указан файл к справочнику баров')

    file_bars_path = sys.argv[1]
    deserializes_json = load_data(file_bars_path)
    if deserializes_json:
        bars = deserializes_json['features']

        longitude = get_gps_coordinates('Введите долготу: ')
        if not longitude:
            exit('долготу должна быть числом, например 33.33')

        latitude = get_gps_coordinates('Введите широту: ')
        if not latitude:
            exit('широта должна быть числом, например 33.33')

        coordinates = [
            longitude,
            latitude
        ]

        bar = get_closest_bar(bars, coordinates)
        output_bar_name('самый близкий бар: ', bar)

        bar = get_biggest_bar(bars)
        output_bar_name('самый большой бар: ', bar)

        bar = get_smallest_bar(bars)
        output_bar_name('самый маленький бар: ', bar)
