#module level

import pytest

pytestmark = pytest.mark.skip(reason="dont want module")

def test_f1():
    print("function1")

class Test_Smoke:
    def test_m1(self):
        print("method1")
    def test_m2(self):
        print("method2")
    def test_m3(self):
        print("method3")

"""
>pytest -vs pyconcept.py
collected 4 items

pyconcept.py::test_f1 SKIPPED (dont want module)
pyconcept.py::Test_Smoke::test_m1 SKIPPED (dont want module)
pyconcept.py::Test_Smoke::test_m2 SKIPPED (dont want module)
pyconcept.py::Test_Smoke::test_m3 SKIPPED (dont want module)
"""