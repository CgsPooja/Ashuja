import pytest

brw = "chrome"
class Test_Facebook:
    def test_login(self):
        print("login pag")
    @pytest.mark.skipif(brw=="chrome", reason="not suporting")
    def test_signup(self):
        print("signup page")
    def test_request(self):
        print("request")

"""
>pytest -vs pyconcept.py
collected 3 items

pyconcept.py::Test_Facebook::test_login login pag
PASSED
pyconcept.py::Test_Facebook::test_signup SKIPPED (not suporting)
pyconcept.py::Test_Facebook::test_request request
PASSED
"""