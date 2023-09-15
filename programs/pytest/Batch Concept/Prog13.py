#multiple class with test method

import pytest

class Fb:
    def test_tc1(self):
        print("fb testcase1")

class Gmail:
    def test_tc2(self):
        print("gmail testcase")
    def test_tc3(self):
        print("gmail testcase3")

"""
>pytest -vs pyconcept.py
collected 0 items
"""