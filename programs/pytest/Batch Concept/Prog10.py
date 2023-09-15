#test class with normal and test method and constructor

import pytest

class Test_FB:
    def __init__(self):
        print("in a constructor")
    def test_login(self):
        print("login page")

"""
>pytest -vs pyconcept.py
collected 0 items
PytestCollectionWarning: cannot collect test class 'Test_FB' because it has a __init__ constructor (from: pyconcept.py)
"""
#the above we are gerring error because a class consist of constructor, constructor will get execute
#only when we create a object, but test class is impicitly callable we no need to create an object.