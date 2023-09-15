import pytest

def test_tc1():
    print("testcase1")
@pytest.mark.smoke
@pytest.mark.skip(reason="not important")
def test_tc2():
    print("testcase2")
@pytest.mark.smoke
def test_tc3():
    print("testcase3")

"""
>pytest -vs -m smoke pyconcept.py
collected 3 items / 1 deselected / 2 selected

pyconcept.py::test_tc2 SKIPPED (not important)
pyconcept.py::test_tc3 testcase3
PASSED
"""