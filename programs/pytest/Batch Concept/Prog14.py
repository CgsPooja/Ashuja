#module level

import pytest

def test_tc1():
    print("test function")

class Test_App:
    def test_tc2(self):
        print("test method1")
    def tc3(self):
        print("test method2")

class Demo:
    def test_tc3(self):
        print("test method3")

"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::test_tc1 test function
PASSED
pyconcept.py::Test_App::test_tc2 test method1
PASSED
"""
