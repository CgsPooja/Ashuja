#test class with normal and test method

import pytest

class TestGmail:
    def TC1(self):
        print("Testcase1")
    def test_TC2(self):
        print("testcase2")

"""
>pytest -vs pyconcept.py
collected 1 item

pyconcept.py::TestGmail::test_TC2 testcase2
PASSED
"""