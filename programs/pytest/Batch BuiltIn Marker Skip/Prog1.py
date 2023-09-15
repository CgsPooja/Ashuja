import pytest

#function level

def test_tc1():
    print("testcase1")
@pytest.mark.skip
def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")

"""
>pytest -vs pyconcept.py
collected 3 items

pyconcept.py::test_tc1 testcase1
PASSED
pyconcept.py::test_tc2 SKIPPED (unconditional skip)
pyconcept.py::test_tc3 testcase3
PASSED
"""