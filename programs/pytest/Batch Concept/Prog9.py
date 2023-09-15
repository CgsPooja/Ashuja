#test class with normal method

import pytest

class TestGmail:
    def TC1(self):
        print("Testcase1")
    def TC2(self):
        print("testcase2")

"""
>pytest -vs pyconcept.py
collected 0 items
"""