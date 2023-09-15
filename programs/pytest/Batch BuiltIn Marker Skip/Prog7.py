import pytest

class Test_Smoke:
    @pytest.mark.c1
    def test_m1(self):
        print("method1")
    @pytest.mark.skip(reason="not a opart of suite")
    def test_m2(self):
        print("method2")
    def test_m3(self):
        print("method3")

"""
collected 3 items / 2 deselected / 1 selected

pyconcept.py::Test_Smoke::test_m1 method1
PASSED
"""