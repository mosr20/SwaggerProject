import json

import jsonpath as jsonpath
import requests

from Extensions.ApiAction import GetMethod
from Extensions.Verfications import VeriyStatusCode, VerifyStatus


def test_get_veriystatusCode():
    VeriyStatusCode(GetMethod("https://petstore.swagger.io/v2/pet/findByStatus?status=available"), 200)

def test_get_VerifyStatus():
    VerifyStatus(GetMethod("https://petstore.swagger.io/v2/pet/findByStatus?status=available"), 'available')







#r = requests.post("https://petstore.swagger.io/v2/pet", json=data)

#r = requests.put("https://petstore.swagger.io/v2/pet", json=data)
