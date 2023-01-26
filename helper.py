import json

import jsonpath

from Extensions.ApiAction import  GetMethod
from Utilities.Base import Set_config
data = {"id":770,"category":{"id":770,"name":"string"},"name":"moshe","photoUrls":["string"],"tags":[{"id":0,"name":"string"}],"status":"available"}
r = GetMethod(Set_config.send_get())
e = json.loads(r.text)
print(e)


