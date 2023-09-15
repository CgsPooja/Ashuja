import pytest

#multiple test function

def test_login():
    print("login testcase")
def test_signup():
    print("signup testcase")
def test_register():
    print("register testcase")
"""
>pytest -vs pyconcept.py
collected 3 items

pyconcept.py::test_login login testcase
PASSED
pyconcept.py::test_signup signup testcase
PASSED
pyconcept.py::test_register register testcase
PASSED
"""