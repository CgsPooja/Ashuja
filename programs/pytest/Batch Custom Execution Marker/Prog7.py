import pytest

class Test_FB:
    @pytest.mark.critical
    def test_reqst(self):
        print("request module")
    @pytest.mark.major
    def test_like(self):
        print("like feature")
    @pytest.mark.critical
    def test_comment(self):
        print("comment feature")

"""
>pytest -vs -m "not major" pyconcept.py
collected 3 items / 1 deselected / 2 selected

pyconcept.py::Test_FB::test_reqst request module
PASSED
pyconcept.py::Test_FB::test_comment comment feature
PASSED
"""
