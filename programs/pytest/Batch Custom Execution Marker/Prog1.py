#function level

import pytest

@pytest.mark.smoke
def test_login():
    print("login page")
@pytest.mark.smoke
def test_compose():
    print("compose page")
def test_tras():
    print("tash module")
def test_bin():
    print("bin module")
@pytest.mark.smoke
def test_inbox():
    print("inbox module")

"""
>pytest -vs -m smoke pyconcept.py
collected 5 items / 2 deselected / 3 selected

pyconcept.py::test_login login page
PASSED
pyconcept.py::test_compose compose page
PASSED
pyconcept.py::test_inbox inbox module
PASSED
"""
