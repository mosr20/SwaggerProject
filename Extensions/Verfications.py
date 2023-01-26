from Extensions.ApiAction import parsJson


def VerifyStatusCode(r, Expect_Code):
    assert r.status_code == Expect_Code


def VerifyStatus(r ,Expect_Status):
    r = parsJson(r)
    for i in r:
        assert i["status"] ==Expect_Status

def VerifyContent_Type(r, Expect_Content_Type):
    assert r.headers.get('Content-Type') == Expect_Content_Type

def Verify_Value_From_Get(r, Expect_Value):
    q = parsJson(r)
    assert Expect_Value in q



