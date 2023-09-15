import pytest

def test_tc1():
    print("testcsae1")

def test_tc4():
    print("testcsae4")

"""
batch execution:
****************
*running multiple test file/module at one shot is called as batch execution.
*store all pytest file in one folder and run it.
command:
--------
    >>cd path_of_all_pytestfile
    >>pytest -vs 
"""
"""
>pytest -vs
collected 4 items

test_tc3.py::test_tc3 testcsae3
PASSED
test_tc3.py::test_tc6 testcsae6
PASSED
test_tc1.py::test_tc1 testcsae1
PASSED
test_tc1.py::test_tc4 testcsae4
PASSED
"""