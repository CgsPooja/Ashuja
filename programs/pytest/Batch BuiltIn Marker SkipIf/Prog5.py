import pytest

#method level with skipif

brw = "mozilla"
class Test_Facebook:
    def test_login(self):
        print("login pag")
    @pytest.mark.skipif(brw=="chrome", reason="not suporting")
    def test_signup(self):
        print("signup page")
    def test_request(self):
        print("request")

"""
collected 3 items

pyconcept.py::Test_Facebook::test_login login pag
PASSED
pyconcept.py::Test_Facebook::test_signup signup page
PASSED
pyconcept.py::Test_Facebook::test_request request
PASSED
"""