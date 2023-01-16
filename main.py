import json

import requests

from Extensions.ApiAction import GetMethod, PostMethod
from Extensions.Verfications import  VerifyStatus, VerifyContent_Type,VerifyStatusCode
from Utilities.Base import Set_config, Create_object

kkk  = {
  "id": 100,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
reqjs = json.dumps(kkk)
loader = json.loads(reqjs)

def test_get_verify_statusCode():
    VerifyStatusCode(GetMethod(Set_config.send_get()), 200)


def test_get_VerifyStatus():
    VerifyStatus(GetMethod(Set_config.send_get()), 'available')

def test_get_Verify_Content_Type():
    VerifyContent_Type(GetMethod(Set_config.send_get()), 'application/json')

def test_post_verify_statusCode():
    VerifyStatusCode(PostMethod(Set_config.send_post(),Create_object.build_message),200)


ddd = Create_object
print(Create_object.build_message())
print(type(kkk))



r = requests.post('https://petstore.swagger.io/v2/pet',loader)
print(r.status_code)


#r = requests.post(Set_config.send_post(), json=Create_object.build_message())
#print(r.text)

#r = requests.put(Set_config.send_put(), json=Create_object.build_message())
#print(r.text)


# pytest --alluredir D:\SwaggerProject\Report main.py
# allure serve D:\SwaggerProject\Report
