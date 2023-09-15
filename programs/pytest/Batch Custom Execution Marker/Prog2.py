import pytest

@pytest.mark.smoke
def test_login():
    print("login page")
@pytest.mark.sanity
def test_compose():
    print("compose page")
@pytest.mark.smoke
def test_tras():
    print("tash module")
@pytest.mark.sanity
def test_bin():
    print("bin module")
@pytest.mark.smoke
def test_inbox():
    print("inbox module")

"""
>pytest -vs -m sanity pyconcept.py
collected 5 items / 3 deselected / 2 selected

pyconcept.py::test_compose compose page
PASSED
pyconcept.py::test_bin bin module
PASSED
"""
