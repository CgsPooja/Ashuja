import pytest

@pytest.mark.regression
@pytest.mark.smoke
def test_login():
    print("login page")
@pytest.mark.sanity
def test_compose():
    print("compose page")
@pytest.mark.regression
@pytest.mark.sanity
def test_trash():
    print("tash module")
@pytest.mark.sanity
def test_bin():
    print("bin module")
@pytest.mark.smoke
def test_inbox():
    print("inbox module")

"""
>pytest -vs -m "smoke or regression" pyconcept.py
collected 5 items / 2 deselected / 3 selected

pyconcept.py::test_login login page
PASSED
pyconcept.py::test_trash tash module
PASSED
pyconcept.py::test_inbox inbox module
PASSED
"""

