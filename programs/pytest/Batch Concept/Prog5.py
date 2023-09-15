import pytest

#normal/non test function
def login():
    print("login testcase")
def signup():
    print("signup testcase")
def register():
    print("register testcase")

"""
>pytest -vs pyconcept.py
collected 0 items
"""