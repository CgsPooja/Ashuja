import pytest

tid = 55
def test_tc1():
    print("testcase1")
@pytest.mark.regression
@pytest.mark.skipif(tid>345, reason="this testcase not included as part of automation")
def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")

"""
>pytest -vs -m "regression" pyconcept.py
collected 3 items / 2 deselected / 1 selected

pyconcept.py::test_tc2 testcase2
PASSED
"""