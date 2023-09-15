import pytest

#class and method level
#testclass and test method
class Test_Gmail:
    def test_TC1(self):
        print("Testcase1")
    def test_TC2(self):
        print("testcase2")
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::Test_Gmail::test_TC1 Testcase1
PASSED
pyconcept.py::Test_Gmail::test_TC2 testcase2
PASSED
"""