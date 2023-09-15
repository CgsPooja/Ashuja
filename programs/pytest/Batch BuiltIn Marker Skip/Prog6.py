import pytest

#method level

class Test_Smoke:
    def test_m1(self):
        print("method1")
    @pytest.mark.skip(reason="not a opart of suite")
    def test_m2(self):
        print("method2")
    def test_m3(self):
        print("method3")

"""
>pytest -vs pyconcept.py
collected 3 items

pyconcept.py::Test_Smoke::test_m1 method1
PASSED
pyconcept.py::Test_Smoke::test_m2 SKIPPED (not a opart of suite)
pyconcept.py::Test_Smoke::test_m3 method3
PASSED
"""