import pytest

pytestmark = pytest.mark.skip(reason="picked for next cycle")

def test_tc1():
    print("testcsae1")

def test_tc4():
    print("testcsae4")
"""
batch execution:
"""
"""
>pytest -vs
collected 8 items

test_tc1.py::test_tc1 SKIPPED (picked for next cycle)
test_tc1.py::test_tc4 SKIPPED (picked for next cycle)
test_tc2.py::test_tc2 SKIPPED (os not supporting)
test_tc2.py::test_tc5 SKIPPED (os not supporting)
test_tc3.py::test_tc3 testcsae3
XPASS (still in progress)
test_tc3.py::test_tc6 testcsae6
XPASS (still in progress)
test_tc4.py::test_tc7 testcsae1
PASSED
test_tc4.py::test_tc8 testcsae4
PASSED
"""