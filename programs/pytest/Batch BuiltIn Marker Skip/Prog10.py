import pytest

@pytest.mark.skip(reason="not a opart of suite")
class Test_Smoke:
    def test_m1(self):
        print("method1")
    def test_m2(self):
        print("method2")
    def test_m3(self):
        print("method3")

class Test_Sanity:
    def test_m4(self):
        print("method1")
    @pytest.mark.skip(reason="not a opart of suite")
    def test_m5(self):
        print("method2")
    def test_m6(self):
        print("method3")

"""
>pytest -vs pyconcept.py
collected 6 items

pyconcept.py::Test_Smoke::test_m1 SKIPPED (not a opart of suite)
pyconcept.py::Test_Smoke::test_m2 SKIPPED (not a opart of suite)
pyconcept.py::Test_Smoke::test_m3 SKIPPED (not a opart of suite)
pyconcept.py::Test_Sanity::test_m4 method1
PASSED
pyconcept.py::Test_Sanity::test_m5 SKIPPED (not a opart of suite)
pyconcept.py::Test_Sanity::test_m6 method3
PASSED
"""