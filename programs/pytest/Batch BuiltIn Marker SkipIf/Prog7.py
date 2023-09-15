import pytest

#class level with skipif

brw = "ie"
@pytest.mark.skipif(brw in ["safari", "opera", "ie"], reason="not suporting")
class Test_Facebook:
    def test_login(self):
        print("login pag")
    def test_signup(self):
        print("signup page")
class Test_Insta:
    def test_request(self):
        print("request")

""""
>pytest -vs pyconcept.py
collected 3 items

pyconcept.py::Test_Facebook::test_login SKIPPED (not suporting)
pyconcept.py::Test_Facebook::test_signup SKIPPED (not suporting)
pyconcept.py::Test_Insta::test_request request
PASSED
"""