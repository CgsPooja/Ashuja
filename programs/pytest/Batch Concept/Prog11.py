#multiple test class with test method

import pytest

class Test_Fb:
    def test_tc1(self):
        print("fb testcase1")

class Test_Gmail:
    def test_tc2(self):
        print("gmail testcase")

"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::Test_Fb::test_tc1 fb testcase1
PASSED
pyconcept.py::Test_Gmail::test_tc2 gmail testcase
PASSED
"""