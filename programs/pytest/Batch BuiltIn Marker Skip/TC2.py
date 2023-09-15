import pytest

os = "mac"
pytestmark = pytest.mark.skipif(os in ['mac', 'linux'], reason="os not supporting")

def test_tc2():
    print("testcase2")

def test_tc5():
    print("testcsae5")