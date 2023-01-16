import json

import requests


def GetMethod(path):
    try:
        r = requests.get(path)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def PostMethod(path, obj):
    try:
        fix_obj = json.loads(obj)
        r = requests.post(path, fix_obj)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def PutMethod(path, obj):
    try:
        r = requests.put(path, obj)
        return r
    except requests.exceptions.RequestException as e:
        print(e)


def DeleteMethod(id):
    try:
        r = requests.delete(id)
        return r
    except requests.exceptions.RequestException as e:
        print(e)

def parsJson(r):
    parse = json.loads(r.text)
    return parse





