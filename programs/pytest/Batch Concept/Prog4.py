import pytest

#combination of test and normal function
def test_login():
    print("login testcase")
def signup():
    print("signup testcase")
def test_register():
    print("register testcase")
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::test_login login testcase
PASSED
pyconcept.py::test_register register testcase
PASSED
"""