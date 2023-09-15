import pytest

class Test_FB:
    @pytest.mark.critical
    def test_reqst(self):
        print("request module")
    @pytest.mark.major
    def test_like(self):
        print("like feature")
    @pytest.mark.critical
    def test_comment(self):
        print("comment feature")

class Test_Insta:
    @pytest.mark.important
    @pytest.mark.critical
    def test_reels(self):
        print("reels module")
    @pytest.mark.minior
    def test_post(self):
        print("post module")
    @pytest.mark.major
    def test_story(self):
        print("story module")

"""
>pytest -vs -m "critical and important" pyconcept.py
collected 6 items / 5 deselected / 1 selected

pyconcept.py::Test_Insta::test_reels reels module
PASSED
"""
