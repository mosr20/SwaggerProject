import requests

from Extensions.ApiAction import GetMethod
from Extensions.Verfications import VeriyStatusCode, VerifyStatus
from Utilities.Base import Set_config, Create_object


def test_get_veriystatusCode():
    VeriyStatusCode(GetMethod(Set_config.send_get()), 200)


def test_get_VerifyStatus():
    VerifyStatus(GetMethod(Set_config.send_get()), 'available')



r = requests.post(Set_config.send_post(), json=Create_object.build_message())
print(r.text)

r = requests.put(Set_config.send_put(), json=Create_object.build_message())
print(r.text)


# pytest --alluredir D:\SwaggerProject\Report main.py
# allure serve D:\SwaggerProject\Report
