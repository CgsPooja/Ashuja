#module level

import pytest

pytestmark = pytest.mark.basic

def test_fun1():
    print("function level")

class Test_cls:
    def test_m1(self):
        print("method1 level")
    def test_m2(self):
        print("method2 level")

"""
>pytest -vs -m basic pyconcept.py
collected 3 items

pyconcept.py::test_fun1 function level
PASSED
pyconcept.py::Test_cls::test_m1 method1 level
PASSED
pyconcept.py::Test_cls::test_m2 method2 level
PASSED
"""
