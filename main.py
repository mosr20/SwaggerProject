import pytest

from Extensions.ApiAction import GetMethod, PostMethod, parsJson, PutMethod
from Extensions.Verfications import VerifyStatus, VerifyContent_Type, VerifyStatusCode,Verify_Value_From_Get
from Log.logger import Creatinglog
from Utilities.Base import Set_config, Create_object

@pytest.mark.get
def test_get_verify_statusCode():
    VerifyStatusCode(GetMethod(Set_config.send_get()),200)

@pytest.mark.get
def test_get_VerifyStatus():
    VerifyStatus(GetMethod(Set_config.send_get()), 'available')
@pytest.mark.get
def test_get_Verify_Content_Type():
    VerifyContent_Type(GetMethod(Set_config.send_get()), 'application/json')
@pytest.mark.post
def test_post_verify_statusCode():
    VerifyStatusCode(PostMethod(Set_config.send_post(),Create_object.build_message()),200)
@pytest.mark.post
def test_post_verify_post():
    Verify_Value_From_Get(GetMethod(Set_config.send_get()),parsJson((PostMethod(Set_config.send_post(),Create_object.build_message()))))
@pytest.mark.post
def test_put_verify_statusCode():
    VerifyStatusCode(PutMethod(Set_config.send_put(),Create_object.build_message()),415)
    Creatinglog("SwaggerProject")










#####Run Test For Report#####
# Enter:  pytest --alluredir D:\SwaggerProject\Report main.py

##### Up Server Allure Report#####
# Enter:  allure serve D:\SwaggerProject\Report
