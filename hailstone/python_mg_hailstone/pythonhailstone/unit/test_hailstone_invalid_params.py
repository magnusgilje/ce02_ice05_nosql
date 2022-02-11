import sys
import pytest
sys.path.insert(0,"..")
import hailstone

def test_hailstone_starting_minus_1():

    with pytest.raises(Exception) as error_info:
        myH = hailstone.Hailstone(-1)

def test_hailstone_starting_0():
    with pytest.raises(Exception) as error_info:
        myC = hailstone.Hailstone(0)
