#class level

import pytest

@pytest.mark.level1
class Test_FB:
    def test_reqst(self):
        print("request module")
    def test_like(self):
        print("like feature")
class Test_Twitter:
    def test_comment(self):
        print("comment feature")
@pytest.mark.level1
class Test_Insta:
    def test_reels(self):
        print("reels module")
    def test_post(self):
        print("post module")
class Test_Gmail:
    def test_story(self):
        print("story module")

"""
>pytest -vs -m "level1" pyconcept.py
collected 6 items / 2 deselected / 4 selected

pyconcept.py::Test_FB::test_reqst request module
PASSED
pyconcept.py::Test_FB::test_like like feature
PASSED
pyconcept.py::Test_Insta::test_reels reels module
PASSED
pyconcept.py::Test_Insta::test_post post module
PASSED
"""
