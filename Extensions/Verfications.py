from Extensions.ApiAction import parsJson


def VeriyStatusCode(r, Expect_Code):
    assert r.status_code == Expect_Code


def VerifyStatus(r ,Expect_Status):
    r = parsJson(r)
    for i in r:
        assert i["status"] ==Expect_Status
