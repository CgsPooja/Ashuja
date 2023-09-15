import pytest

tid = 555
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
pyconcept.py::test_tc2 SKIPPED (this testcase not included as part of automation)
"""