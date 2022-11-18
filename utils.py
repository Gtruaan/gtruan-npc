import json
import os

def param(key):
    '''
    key -> params[key]
    '''
    path = os.path.join('parameters.json')

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data[key]