import pytest

pytestmark = pytest.mark.imp

def test_tc1():
    print("testcsae1")

def test_tc4():
    print("testcsae4")
"""
marker in batch execution
"""
"""
>pytest -vs -m "imp"
collected 6 items / 2 deselected / 4 selected

test_tc1.py::test_tc1 testcsae1
PASSED
test_tc1.py::test_tc4 testcsae4
PASSED
test_tc3.py::test_tc3 testcsae3
PASSED
test_tc3.py::test_tc6 testcsae6
PASSED
"""
