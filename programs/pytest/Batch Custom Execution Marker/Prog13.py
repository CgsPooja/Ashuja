#class and method level

import pytest

@pytest.mark.level1
class Test_FB:
    @pytest.mark.f1
    def test_reqst(self):
        print("request module")
    @pytest.mark.f2
    def test_like(self):
        print("like feature")
class Test_Twitter:
    def test_comment(self):
        print("comment feature")
@pytest.mark.level1
class Test_Insta:
    @pytest.mark.f1
    def test_reels(self):
        print("reels module")
    def test_post(self):
        print("post module")
class Test_Gmail:
    @pytest.mark.f1
    def test_story(self):
        print("story module")

"""
>pytest -vs -m "level1 and f1" pyconcept.py
collected 6 items / 4 deselected / 2 selected

pyconcept.py::Test_FB::test_reqst request module
PASSED
pyconcept.py::Test_Insta::test_reels reels module
PASSED
"""
